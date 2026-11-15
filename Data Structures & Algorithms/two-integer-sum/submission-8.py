class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIdx = {}
        for i, n in enumerate(nums):
            numToIdx[n] = i
        for i, n in enumerate(nums):
            val = target - n
            if val in numToIdx and i != numToIdx[val]:
                return [i, numToIdx[val]]
        return []