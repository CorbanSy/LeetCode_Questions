class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            # Edge case: if needle is empty
        if not needle:
            return 0
        
        # Lengths of haystack and needle
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        # Edge case: if needle is longer than haystack
        if needle_len > haystack_len:
            return -1
        
        # Sliding window approach
        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i
        
        return -1