class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Function to perform backtracking
        def backtrack(index: int, current_combination: str):
            # Base case: if the current combination is the same length as digits
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get the letters that the current digit maps to
            letters = digit_to_letters[digits[index]]
            for letter in letters:
                # Append the current letter to the combination and proceed to the next digit
                backtrack(index + 1, current_combination + letter)
        
        result = []
        backtrack(0, "")
        return result