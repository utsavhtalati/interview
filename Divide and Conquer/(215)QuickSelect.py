# 215. Kth largest element in an Array

####### Given an integer array nums and an integer k, return the kth largest element in the array.
####### Note that it is the kth largest element in the sorted order, not the kth distinct element.
####### Can you solve it without sorting?

# Algorithm: This algorithm requires a divide and conquer solution: utilizes both QuickSort and Binary Search attributes

"""

1. Find a pivot value from the list and partition the left and right side of the partition. 
2. If the kth largest element is the pivot -> return pivot.
2. Else if the kth largest element is greater than the pivot then 
   - divide and conquer the right hand side
3. Else divide and conquer the left hand side.

Run-time of the algorithm:

(First Partitioning after the pivot is chosen takes n time.) n
(We half the problem each time due to the kth largest condition) nlogn
(Overall run-time O(n) ) 

"""



# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pivot_index) -> int:
            pivot_value = nums[pivot_index]
            # Move pivot to the end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            # Move all smaller elements to the left
            for i in range(left, right):
                if nums[i] > pivot_value:  # Note: '>' for k-th largest
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
            # Move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def select(left: int, right: int, k_smallest: int) -> int:
            if left == right:  # If the list contains only one element
                return nums[left]
            # Select a random pivot_index
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            # The pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)
