class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        res = 0
        charCount = {}

        for end in range(len(s)):
            charCount[s[end]] = 1 + charCount.get(s[end], 0)
            while ((end - start + 1) - max(charCount.values())) > k:
                charCount[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        
        return res
                