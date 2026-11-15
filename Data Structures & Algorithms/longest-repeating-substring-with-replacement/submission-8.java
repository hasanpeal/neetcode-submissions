class Solution 
{
    public int characterReplacement(String s, int k) 
    {
        int[] ch = new int[26];

        int start = 0, currCharCount = 0, maxCount = 0, maxLength = 0;

        for(int end = 0; end < s.length(); end++)
        {
          ch[s.charAt(end) - 'A']++;
          currCharCount = ch[s.charAt(end) - 'A'];
          maxCount = Math.max(maxCount, currCharCount);
          int windowLength = end - start + 1;
          while(windowLength - maxCount > k)
          {
            ch[s.charAt(start) - 'A']--;
            start++;
            windowLength = end - start + 1;
          }
          maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
    }
}
