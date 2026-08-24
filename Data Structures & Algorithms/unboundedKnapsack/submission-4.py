class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M = capacity
        N = len(profit)

        cache = [[-1] * (M + 1) for _ in range(N)]

        def helper(index, capacity):
            if index == len(profit):
                return 0
            if cache[index][capacity] != -1:
                return cache[index][capacity]

            #skip
            cache[index][capacity] = helper(index + 1, capacity)

            newCap = capacity - weight[index]
            if newCap >= 0:
                include = profit[index] + helper(index, newCap)
                cache[index][capacity] = max(cache[index][capacity], include)

            return cache[index][capacity]

        return helper(0, capacity)
