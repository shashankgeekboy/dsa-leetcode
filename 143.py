class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Init
        results = 0
        dp = [{} for _ in range(len(nums))]
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        # Count
        for i in range(len(nums)):
            for j in range(i):
                # 32 bit limit
                diff = nums[i] - nums[j]
                if diff > INT_MAX or diff < INT_MIN:
                    continue
                    
                # Records
                dp[i][diff] = dp[i].get(diff, 0) + 1
                if diff in dp[j]:
                    results += dp[j][diff]
                    dp[i][diff] += dp[j][diff]
                
        return results
