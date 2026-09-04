class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}

        def helper(index, coin_held, cooldown = False):
            if index >= len(prices):
                return 0
            ids = (index, coin_held, cooldown)
            if ids in cache:
                return cache[ids]

            max_profit = helper(index + 1, coin_held, False)

            if coin_held != -1: # Sell
                newProfit = prices[index] - coin_held + helper(index + 1, -1, True)
                max_profit = max(max_profit, newProfit)
            elif not cooldown: # Buy
                newProfit = helper(index + 1, prices[index], False)
                max_profit = max(max_profit, newProfit)

            cache[ids] = max_profit
            return max_profit

        return helper(0, -1)

            
        