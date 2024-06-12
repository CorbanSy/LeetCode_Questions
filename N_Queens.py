class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            board = []
            for i in range(n):
                row = ['.'] * n
                row[state[i]] = 'Q'
                board.append("".join(row))
            return board
        
        def is_valid(state, row, col):
            for r in range(row):
                c = state[r]
                if c == col or abs(c - col) == abs(r - row):
                    return False
            return True
        
        def solve(row, state):
            if row == n:
                result.append(create_board(state))
                return
            for col in range(n):
                if is_valid(state, row, col):
                    state[row] = col
                    solve(row + 1, state)
                    state[row] = -1
        
        result = []
        state = [-1] * n
        solve(0, state)
        return result