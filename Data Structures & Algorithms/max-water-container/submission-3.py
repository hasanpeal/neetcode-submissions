class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        maxArea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            maxArea = max(maxArea, height*width)
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return maxArea
