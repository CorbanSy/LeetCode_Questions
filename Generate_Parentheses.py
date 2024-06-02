class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # If the current string is well-formed and has the correct length, add it to the result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # If we can add an open parenthesis, do so
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # If we can add a close parenthesis, do so
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        # Start the backtracking process with an empty string and 0 open and close counts
        backtrack("", 0, 0)
        
        return result