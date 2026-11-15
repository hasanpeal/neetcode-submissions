class Solution {
    public int maxProfit(int[] prices) {
        int left = 0, profit = 0, maxProfit = 0;
        int right = 1;
        while(right < prices.length){
          profit = prices[right] - prices[left];
          maxProfit = Math.max(maxProfit, profit);
          if(profit < 0){
            left = right;
            right++;
          } else right++;
        }
        if(maxProfit < 0) maxProfit = 0;
        return maxProfit;
    }
}
