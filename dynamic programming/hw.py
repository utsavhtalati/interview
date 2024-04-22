# Define the array of values for the items
values = [10, 24, 5, 9, 6]

# Initialize the DP array with 0's
n = len(values)
dp = [[0]*n for _ in range(n)]

# Fill in the base cases where i == j, Stellar can only take one item
for i in range(n):
    dp[i][i] = values[i]

# Fill in the rest of the DP array
# We fill the table diagonally because we can only solve for dp[i][j] if we know
# the solutions for smaller ranges dp[i+1][j-1], dp[i+2][j], and dp[i][j-2]
for length in range(2, n+1):  # length of the range of items being considered
    for i in range(n - length + 1):
        j = i + length - 1
        # If Stellar picks the ith item, Sage will pick (i+1)th or jth item next
        # We take the minimum because Sage is trying to minimize Stellar's value
        take_i = values[i] + min(dp[i+2][j] if (i+2) <= j else 0, dp[i+1][j-1] if i+1 <= j-1 else 0)
        # If Stellar picks the jth item, Sage will pick ith or (j-1)th item next
        take_j = values[j] + min(dp[i+1][j-1] if i+1 <= j-1 else 0, dp[i][j-2] if i <= j-2 else 0)
        # Stellar wants to maximize her value, so we take the max
        dp[i][j] = max(take_i, take_j)

# Display the filled DP table
print(dp)
