class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet <Integer> set = new HashSet<>();
        for(int n: nums){
          set.add(n);
        }
        int count = 0;
        int maxCount = 0;

        for(int i = 0; i < nums.length; i++) {
          int curr = nums[i];
          count = 1;
          if(!set.contains(curr-1)){
            while(set.contains(curr+1)){
              curr += 1;
              count++;
            }
            if(count > maxCount) maxCount = count;
          }
        }
        return maxCount;
    }
}
