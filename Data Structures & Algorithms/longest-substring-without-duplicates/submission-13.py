class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        end = 0
        seen = set()

        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                res = max(len(seen), res)
                end += 1
            else:
                seen.remove(s[start])
                start += 1
        
        return res