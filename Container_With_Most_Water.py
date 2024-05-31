class Solution:
    def maxArea(self, height: list[int]) -> int:
         # Initialize two pointers and the maximum area
        left, right = 0, len(height) - 1
        max_area = 0
        
        # Iterate until the two pointers meet
        while left < right:
            # Calculate the width and height of the current container
            width = right - left
            h = min(height[left], height[right])
            
            # Calculate the area and update the maximum area if needed
            current_area = width * h
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area