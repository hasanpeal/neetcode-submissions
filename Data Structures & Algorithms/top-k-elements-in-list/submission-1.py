class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i], 0)
        count = [[] for i in range(len(nums) + 1)]
        for key, val in map.items():
            count[val].append(key)
        res = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
                