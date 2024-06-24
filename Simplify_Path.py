class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Split the path by '/' and process each part
        parts = path.split('/')
        for part in parts:
            if part == '' or part == '.':
                continue  # Skip empty and current directory parts
            elif part == '..':
                if stack:
                    stack.pop()  # Go back one directory
            else:
                stack.append(part)  # Add valid directory to the stack
        
        # Build the canonical path
        simplified_path = '/' + '/'.join(stack)
        return simplified_path