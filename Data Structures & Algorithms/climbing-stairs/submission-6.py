class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(stair):
            if stair == n:
                return 1
            if stair > n:
                return 0

            if stair in cache:
                return cache[stair]

            cache[stair] = helper(stair + 1) + helper(stair + 2)
            return cache[stair]

        return helper(0)

    # 1 + 1 + 1 1 + 2