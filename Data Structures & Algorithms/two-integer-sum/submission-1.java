class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        HashMap <Integer, Integer> map = new HashMap <Integer, Integer> ();
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }

        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(target - nums[i])){
                int index1 = i;
                int index2 = map.get(target - nums[i]);

                if(index1 == index2) continue;

                if(index1 < index2){
                    res[0] = index1;
                    res[1] = index2;
                } else {
                    res[0] = index2;
                    res[1] = index1;
                }
                break;
            }
        }
        return res;
    }
}
