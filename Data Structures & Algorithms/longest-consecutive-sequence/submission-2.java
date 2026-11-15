class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet <Integer> set = new HashSet<>();
        int count = 1;
        int maxCount = 0;
        for(int num: nums) set.add(num);

        for(int i = 0; i < nums.length; i++){
            int curr = nums[i];
            if(!set.contains(curr - 1)){
                while(set.contains(curr + 1)){
                    count++;
                    curr++;
                }
                maxCount = Math.max(count, maxCount);
                count = 1;
            }
        }
        return maxCount;
    }
}
