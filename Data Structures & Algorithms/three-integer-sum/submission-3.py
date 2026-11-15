class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        has = {}
        for i, v in enumerate(nums):
            has[v] = i
        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1):
                key = -nums[i] - nums[j]
                if key in has and has.get(key) != i and has.get(key) != j:
                    triplet = [nums[i], nums[j], key]
                    triplet.sort()
                    if triplet not in res:
                        res.append(triplet)
        return res