class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Traverse the string
        for char in s:
            rows[current_row] += char
            # Change direction when you reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        
        # Concatenate all rows to form the final string
        return ''.join(rows)
    
solution = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(solution.convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"

numRows = 4
print(solution.convert(s, numRows))  # Output: "PINALSIGYAHRPI"