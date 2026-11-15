class Solution {
    public int maxArea(int[] heights) {
        int start = 0;
        int end = heights.length - 1;
        int max = 0;

        while(start < end){
          int width = end - start;
          int area = width * Math.min(heights[end], heights[start]);
          max = Math.max(max, area);
          if(heights[start] <= heights[end]) start++;
          else end--;
        }
        return max;
    }
}
