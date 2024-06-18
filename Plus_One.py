class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse the digits array from the end
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, just increment it and return the array
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0
            digits[i] = 0
        
        # If all digits are 9, we need to add an additional digit at the beginning
        return [1] + digits