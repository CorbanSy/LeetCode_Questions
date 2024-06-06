class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         # Create sets to keep track of the seen numbers in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    # Calculate the index of the sub-box
                    sub_box_index = (r // 3) * 3 + (c // 3)
                    
                    if (num in rows[r] or
                        num in columns[c] or
                        num in sub_boxes[sub_box_index]):
                        return False
                    
                    rows[r].add(num)
                    columns[c].add(num)
                    sub_boxes[sub_box_index].add(num)
        
        return True