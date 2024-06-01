class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of the opening brackets
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it is not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket does not match the top element, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets were matched, otherwise return False
        return not stack