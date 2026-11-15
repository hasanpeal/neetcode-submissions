class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap <String, List<String>> res = new HashMap <> ();
        for(String curr: strs){
          char[] ch = curr.toCharArray();
          Arrays.sort(ch);
          String word = String.valueOf(ch);
          if(!res.containsKey(word)){
            res.put(word, new ArrayList<>());
            res.get(word).add(curr);
          } else res.get(word).add(curr);
        }
        return new ArrayList<>(res.values());
    }
}
