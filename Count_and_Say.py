class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Start with the first element in the sequence
        result = "1"
        
        for _ in range(1, n):
            result = self.next_sequence(result)
        
        return result
    
    def next_sequence(self, s: str) -> str:
        # Initialize variables
        count = 1
        next_seq = []
        
        # Loop through the string, starting from the second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # Increment the count if the current character is the same as the previous
                count += 1
            else:
                # Append the count and the previous character to the next sequence
                next_seq.append(str(count))
                next_seq.append(s[i - 1])
                # Reset the count
                count = 1
        
        # Append the count and the last character to the next sequence
        next_seq.append(str(count))
        next_seq.append(s[-1])
        
        # Join the list into a string and return
        return ''.join(next_seq)