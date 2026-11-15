class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        has = set()
        for num in nums:
            has.add(num)
        for i in range(len(nums)):
            curr = nums[i]
            high = 1
            if curr - 1 in has:
                continue
            while curr + 1 in has:
                curr += 1
                high += 1
            res = max(res, high)
        return res
            
