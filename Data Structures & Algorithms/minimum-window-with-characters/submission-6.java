class Solution {
    public String minWindow(String s, String t) {
        int start = 0;
        int minWindow = Integer.MAX_VALUE;
        int minStart = 0;
        HashMap <Character, Integer> need = new HashMap<>();
        HashMap <Character, Integer> have = new HashMap<>();
        int haveCount = 0;
        int needCount = t.length();
        for(int i = 0; i < t.length(); i++) {
          char ch = t.charAt(i);
          need.put(ch, need.getOrDefault(ch, 0) + 1);
        }
        for(int end = 0; end < s.length(); end++){
          char endChar = s.charAt(end);
          if(need.containsKey(endChar)){
            have.put(endChar, have.getOrDefault(endChar, 0) + 1);
            if(have.get(endChar) <= need.get(endChar)) haveCount++;
            while(haveCount == needCount){
              char startChar = s.charAt(start);
              if(end - start + 1 < minWindow){
                minStart = start;
                minWindow = end - start + 1;
              }
              if(need.containsKey(startChar)){
                have.put(startChar, have.get(startChar) - 1);
                if(have.get(startChar) < need.get(startChar)){
                  haveCount--;
                }
              }
              start++;
            }
          }
        }
        return minWindow > s.length() ? "": s.substring(minStart, minStart + minWindow);
    }
}
