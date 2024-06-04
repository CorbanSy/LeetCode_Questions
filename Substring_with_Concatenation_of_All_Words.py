from collections import Counter
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        words_count = Counter(words)
        
        result = []
        
        for i in range(len(s) - total_len + 1):
            seen = Counter()
            j = 0
            while j < num_words:
                word_start = i + j * word_len
                word = s[word_start:word_start + word_len]
                if word in words_count:
                    seen[word] += 1
                    if seen[word] > words_count[word]:
                        break
                else:
                    break
                j += 1
            if j == num_words:
                result.append(i)
        
        return result