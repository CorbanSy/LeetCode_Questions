class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            # If the combination is done
            if len(path) == k:
                result.append(path[:])
                return
            
            # Go through all numbers from 'start' to 'n'
            for i in range(start, n + 1):
                # Add i into the current combination
                path.append(i)
                # Use next integers to complete the combination
                backtrack(i + 1, path)
                # Backtrack, remove i from the current combination
                path.pop()
        
        result = []
        backtrack(1, [])
        return result
