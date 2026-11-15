class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
        HashMap <Character, Integer> res = new HashMap <Character, Integer> ();
        HashMap <Character, Integer> res2 = new HashMap <Character, Integer> ();
        for(int i = 0; i < s.length(); i++) {
            if(res.get(s.charAt(i)) == null){
                res.put(s.charAt(i), 1);
            } else {
                res.put(s.charAt(i), res.get(s.charAt(i)) + 1);
            }
        }

        for(int i = 0; i < t.length(); i++) {
            if(res2.get(t.charAt(i)) == null){
                res2.put(t.charAt(i), 1);
            } else {
                res2.put(t.charAt(i), res2.get(t.charAt(i)) + 1);
            }
        }

        return res.equals(res2);
    }
}
