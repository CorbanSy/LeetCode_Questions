class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with a base value to handle edge cases
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '(' onto the stack
            else:
                stack.pop()  # Pop the topmost element
                if not stack:
                    stack.append(i)  # If stack is empty, push the current index as the base for the next valid substring
                else:
                    max_length = max(max_length, i - stack[-1])  # Calculate the length of the current valid substring
        
        return max_length