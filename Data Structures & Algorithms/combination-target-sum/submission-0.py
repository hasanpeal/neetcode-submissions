class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        for num in nums:
            for i in range(1, target + 1):
                if num > i:
                    continue
                if num == i:
                    dp[i].append([num])
                else:
                    for combo in dp[i - num]:
                        dp[i].append(combo + [num])
        return dp[target]