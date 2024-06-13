class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Precompute factorials
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        
        # Convert k to 0-based indexing
        k -= 1
        
        # List of numbers to get permutations from
        numbers = list(range(1, n + 1))
        permutation = []
        
        # Generate k-th permutation
        for i in range(n, 0, -1):
            # Determine the index of the current digit
            index = k // factorial[i - 1]
            permutation.append(str(numbers[index]))
            # Remove used number and update k
            numbers.pop(index)
            k %= factorial[i - 1]
        
        return ''.join(permutation)