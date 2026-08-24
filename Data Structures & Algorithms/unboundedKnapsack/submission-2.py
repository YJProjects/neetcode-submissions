class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        def helper(index, capacity):
            if index == len(profit):
                return 0
            if (index, capacity) in memo:
                return memo[(index, capacity)]

            maxProfit = helper(index + 1, capacity)

            newCap = capacity - weight[index]
            if newCap >= 0:
                newProfit = profit[index] + helper(index, newCap)
                maxProfit = max(maxProfit, newProfit)

            memo[(index, capacity)] = maxProfit
            return maxProfit

        return helper(0, capacity)
