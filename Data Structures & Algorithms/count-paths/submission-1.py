class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        seen = {}

        def uniquePathsHelper(x, y):
            if not (0 <= x < m) or not (0 <= y < n):
                return 0
            if (x, y) == (m-1, n-1):
                return 1
            if (x, y) in seen:
                return seen[(x, y)]

            total_paths = 0
            total_paths += uniquePathsHelper(x + 1, y)
            total_paths += uniquePathsHelper(x, y + 1)
            
            seen[(x, y)] = total_paths

            return seen[(x, y)]

        return uniquePathsHelper(0, 0)
        