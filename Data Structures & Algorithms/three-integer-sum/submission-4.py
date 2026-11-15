class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ValToIndex = {}
        res = []
        for i in range(len(nums)):
            ValToIndex[nums[i]] = i

        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1):
                key = -nums[i] - nums[j]
                if key in ValToIndex and ValToIndex[key] != i and ValToIndex[key] != j:
                    temp = [nums[i], nums[j], key]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
        
        return res
                
        