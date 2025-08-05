# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # get lowest and highest price and calc difference
        # lowest must be before highest
        # keep track of highest profit possible
        highest_profit = 0
        lowest_price = prices[0]
        if len(prices) <= 1:
            return 0
        for p in prices:
            if p < lowest_price:
                lowest_price = p
            profit = p - lowest_price
            if profit > highest_profit:
                highest_profit = profit
        return highest_profit
# @leet end
