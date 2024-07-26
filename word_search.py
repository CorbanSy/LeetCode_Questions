from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            # Mark the cell as visited by replacing the character with a placeholder
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all possible directions: up, down, left, right
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if backtrack(r + dr, c + dc, index + 1):
                    return True
            
            # Restore the cell value
            board[r][c] = temp
            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and backtrack(row, col, 0):
                    return True
        
        return False
