class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a DP table with default value False
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* that can match an empty string
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    # Direct match or match with '.'
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # Match zero occurrence of p[j-2]
                    dp[i][j] = dp[i][j-2]
                    # Match one or more occurrence of p[j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        
        # The result is whether the entire string s matches the entire pattern p
        return dp[len(s)][len(p)]
