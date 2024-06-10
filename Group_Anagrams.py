from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            # Sort the string to get the anagram signature
            sorted_str = ''.join(sorted(s))
            # Append the original string to the corresponding anagram group
            anagrams[sorted_str].append(s)
        
        # Return all grouped anagrams as a list of lists
        return list(anagrams.values())