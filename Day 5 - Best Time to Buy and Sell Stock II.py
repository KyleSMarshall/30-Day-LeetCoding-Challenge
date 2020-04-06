# Problem:
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example - 
Input: [7,1,5,3,6,4]
Output: 7
'''

# Solution:
'''
My solution is not optimal. I tunneled in on fixing the code I had rather than seeing the easier alternative which
will be posted below this solution. One perk that this solution has over the optimal/easier is that this solution can
return the actual days on which the stocks were bought or sold, the easier solution can only return the maximum profit.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        buy = None
        sell = 0
        profit = 0
        while j < len(prices)-1:
            for i in range(j+1, len(prices)):
            
                if prices[i] > prices[j] and buy is None:
                    buy = prices[j]
                    j = i - 1
                    break
                    
                if prices[i] > sell and buy is not None and prices[i] > buy:
                    sell = prices[i]
                    j = i
                    break
                    
                elif buy is not None and sell != 0:
                    profit += sell - buy
                    buy = None
                    sell = 0
                    break
                    
                j = i
            if i == len(prices) -1 and buy is None:
                break
            elif i == len(prices) -1 and buy is not None:
                sell = prices[-1]
                profit += sell - buy
                break

        return max(profit, 0)
        
      
# Easier Solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
