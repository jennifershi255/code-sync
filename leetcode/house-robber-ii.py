class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
                return 0
        if len(nums) == 2:
                return max(nums[0],nums[1])
        if len(nums) == 1:
            return nums[0]
        
        def solve(n):
            dp = [0] * len(n)
            dp[0] = n[0]
            dp[1] = max(n[0],n[1])

            for i in range(2,len(n)):
                dp[i] = max(dp[i-1], dp[i-2] + n[i])
            
            return dp[-1]

        return max(solve(nums[1:]), solve(nums[:-1]))