class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, right, longest = 0, 0, 0
        while(right < len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                length = right - left + 1
                longest = max(longest, length)
                right += 1
            else:
                seen.clear()
                left += 1
                right = left
        return longest