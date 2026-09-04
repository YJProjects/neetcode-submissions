class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        seen = set()
        res = 0

        def dfs(i, j, prev):
            cords = (i, j)
            if not (0 <= i < len(matrix)): # Invalid x cord
                return 0
            if not (0 <= j < len(matrix[i])): # Invalid y cord
                return 0
            if matrix[i][j] <= prev:
                return 0
            if cords in cache:
                return cache[cords]
            if cords in seen:
                return 0
            
            seen.add(cords)

            max_path = 1 + max(
                dfs(i + 1, j, matrix[i][j]),
                dfs(i - 1, j, matrix[i][j]),
                dfs(i, j + 1, matrix[i][j]),
                dfs(i, j - 1, matrix[i][j])
            )

            cache[cords] = max_path
            return max_path

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, dfs(i, j, -1))

        return res
                