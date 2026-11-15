class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        valToIdx = {}
        res = []
        for i in range(len(nums)):
            valToIdx[nums[i]] = i
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                val = - nums[i] - nums[j]
                if val in valToIdx and valToIdx[val] != i and valToIdx[val] != j:
                    triplet = [nums[i], nums[j], val]
                    triplet.sort()
                    if triplet not in res:
                        res.append(triplet)
        return res
                
        