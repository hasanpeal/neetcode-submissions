class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        ArrayList<List<Integer>> list = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int key = -nums[i] - nums[j];
                if (map.containsKey(key) && map.get(key) != i && map.get(key) != j) {
                    List<Integer> triplet = Arrays.asList(nums[i], nums[j], key);
                    Collections.sort(triplet);
                    if (!list.contains(triplet)) {
                        list.add(triplet);
                    }
                }
            }
        }

        return list;
    }
}
