class Solution:
    def reverse(self, x: int) -> int:
         # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Check if the number is negative and store the sign
        sign = -1 if x < 0 else 1
        
        # Reverse the absolute value of the number
        reversed_x = int(str(abs(x))[::-1])
        
        # Apply the sign to the reversed number
        reversed_x *= sign
        
        # Check if the reversed number is within the 32-bit signed integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x

solution = Solution()

