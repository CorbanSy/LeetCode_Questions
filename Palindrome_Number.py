class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_srt = str(x)

        return x_srt == x_srt[::-1]

solution = Solution()

x = 121
print(solution.isPalindrome(x))  # Output: True

x = -121
print(solution.isPalindrome(x))  # Output: False

x = 10
print(solution.isPalindrome(x))  # Output: False