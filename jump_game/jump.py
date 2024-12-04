def jump(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            if j + nums[j] >= i:
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[n - 1]

# Example:
nums1 = [2,3,1,1,4]
print(jump(nums1))  # Output: 2

nums2 = [2,3,0,1,4]
print(jump(nums2))  # Output: 2