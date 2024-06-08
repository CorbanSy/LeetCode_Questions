class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either of the numbers is zero, the product is zero
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Reverse both strings
        num1, num2 = num1[::-1], num2[::-1]
        
        # Multiply each digit and add the results to the appropriate positions
        for i in range(m):
            for j in range(n):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                result[i + j] += digit1 * digit2
                result[i + j + 1] += result[i + j] // 10  # Carry over
                result[i + j] %= 10
        
        # Convert result array back to a string
        result = result[::-1]  # Reverse the result to the correct order
        # Skip any leading zeros
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        
        result_str = ''.join(map(str, result[start:]))
        
        return result_str
