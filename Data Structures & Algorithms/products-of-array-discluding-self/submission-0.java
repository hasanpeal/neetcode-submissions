class Solution {
    public int[] productExceptSelf(int[] nums) {
        HashMap <Integer, Integer> map = new HashMap <> ();
        int[] ans = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
          map.put(i, nums[i]);
        }
        for(int i = 0; i < nums.length; i++){
          int mult = 1;

          for(int j = 0; j < nums.length; j++){
            if(j == i) continue;
            mult *= map.get(j);
          }
          ans[i] = mult;
        }
        return ans;
    }
}  
