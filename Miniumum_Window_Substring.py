from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Dictionary to count all characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Dictionary to keep track of all the unique characters in the current window
        window_counts = defaultdict(int)
        
        # Formed is used to keep track of how many unique characters in t are present in the current window
        formed = 0
        
        # Left and right pointer
        l, r = 0, 0
        
        # (window length, left, right)
        ans = float("inf"), None, None
        
        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] += 1
            
            # If the current character's count matches the count in t
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # Try to contract the window until it ceases to be 'desirable'
            while l <= r and formed == required:
                character = s[l]
                
                # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # The character at the position pointed by the `left` pointer is no longer a part of the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                # Move the left pointer ahead
                l += 1
            
            # Keep expanding the window by moving the right pointer
            r += 1
        
        # Return the smallest window or an empty string if no such window exists
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

# Example usage:
sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
