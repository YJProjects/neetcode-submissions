class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}

        def helper(index, total):
            if index == len(coins):
                return float('inf')
            if total == amount:
                return 0
            if total > amount:
                return float('inf')
            if (index, total) in cache:
                return cache[(index, total)]
             
            skip = helper(index + 1, total)
            include = 1 + helper(index, total + coins[index])

            cache[(index, total)] = min(skip, include)
            return cache[(index, total)]



        result = helper(0, 0)
        return result if result != float('inf') else -1