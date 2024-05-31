class Solution:
    def myAtoi(self, s: str) -> int:
         # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Initialize the index and the length of the string
        i, n = 0, len(s)
        
        # Ignore leading whitespace
        while i < n and s[i].isspace():
            i += 1
        
        # Check if we reached the end of the string
        if i == n:
            return 0
        
        # Determine the sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Read digits and convert to integer
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        # Apply the sign
        num *= sign
        
        # Clamp the number to the 32-bit signed integer range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num