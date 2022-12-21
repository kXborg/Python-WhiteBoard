# Find maximum non adjacent sum.
# Example 1
# l1 = [1,3,5,6,1,3]        max non adjacent sum = 12
# l2 = [1,3,1,5,2,1,7,2]    max non adjacent sum = 11


def findMaxNonAdjSum(l):
	for i in range(0, len(l)):
		dp[i] = max(pb[i] + dp[i-2], dp[i-1])

l1 = [1,3,5,6,1,3]

findMaxNonAdjSum(l1)