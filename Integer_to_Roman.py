class Solution:
    def intToRoman(self, num: int) -> str:
         # List of tuples mapping integer values to Roman numerals
        val_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        # Initialize the result string
        roman_numeral = ""
        
        # Iterate through the list of tuples
        for value, symbol in val_to_roman:
            # Append the symbol while num is greater than or equal to the value
            while num >= value:
                roman_numeral += symbol
                num -= value
        
        return roman_numeral