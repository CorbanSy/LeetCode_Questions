class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an empty n x n matrix
        matrix = [[0] * n for _ in range(n)]
        
        # Define the initial boundaries
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1  # The number to be filled in the matrix
        
        # Loop until the entire matrix is filled
        while top <= bottom and left <= right:
            # Fill the top row from left to right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Move the top boundary down
            
            # Fill the right column from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Move the right boundary left
            
            # Fill the bottom row from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1  # Move the bottom boundary up
            
            # Fill the left column from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1  # Move the left boundary right
        
        return matrix