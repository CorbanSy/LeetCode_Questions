class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
            # Handle edge case for overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        # Subtract the divisor from dividend until dividend becomes less than divisor
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Apply the sign to the result
        if negative:
            quotient = -quotient

        # Clamp the result to the 32-bit signed integer range
        return max(min(quotient, 2**31 - 1), -2**31)