class Solution {
    public boolean isPalindrome(String s) {
      String newStr = "";
        for(int i = 0; i < s.length(); i++){
          if((s.charAt(i) >= 65 && s.charAt(i) <= 90) || (s.charAt(i) >= 97 && s.charAt(i) <= 122) || (s.charAt(i) >= 48 && s.charAt(i) <= 57)){
            newStr += s.charAt(i);
          }
        }
      
      String newStrII = "";
        for(int i = newStr.length() - 1; i >= 0; i--){
          newStrII += newStr.charAt(i);
        }
      
      System.out.println(newStr.toUpperCase());
      System.out.println(newStrII.toUpperCase());
      return newStr.toUpperCase().equals(newStrII.toUpperCase());
    }
}
