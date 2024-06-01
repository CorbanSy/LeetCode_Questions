class Solution:
    def romanToInt(self, s: str) -> int:
         # Mapping of Roman numerals to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the result
        result = 0
        n = len(s)
        
        # Iterate through the string
        for i in range(n):
            # If the current numeral is less than the next numeral, subtract it
            if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]
            else:
                # Otherwise, add the current numeral to the result
                result += roman_to_int[s[i]]
        
        return result