class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(rowIdx, colIdx, seen, index):
            if index >= len(word):
                return True
            # Check bounds
            if not 0 <= rowIdx < len(board) or not 0 <= colIdx < len(board[rowIdx]):
                return False
            if board[rowIdx][colIdx] != word[index]:
                return False
            if (rowIdx, colIdx) in seen:
                return False
            
            seen.add((rowIdx, colIdx))

            return (
                dfs(rowIdx + 1, colIdx, seen, index + 1) or
                dfs(rowIdx - 1, colIdx, seen, index + 1) or
                dfs(rowIdx, colIdx + 1, seen, index + 1) or
                dfs(rowIdx, colIdx - 1, seen, index + 1) or
                seen.remove((rowIdx, colIdx))
            )


        for rowIdx in range(len(board)):
            for colIdx in range(len(board[rowIdx])):
                seen = set()
                if dfs(rowIdx, colIdx, seen, 0):
                    return True
        return False
        