class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # # Solution 1: 
    #     # Check: If s and t are not the same length, then not valid anagrams
    #     if len(s) != len(t):
    #         return False

    #     # Sort both strings
    #     sortedS = sorted(s)
    #     sortedT = sorted(t)

    #     # Iterate through each i, char in s
    #     for i, char in enumerate(sortedS):
    #         # If char in s does not equal same indexed letter in t, return false
    #         if char != sortedT[i]:
    #             return False

    #     # Otherwise, if no early return, then valid anagram. return true 
    #     return True

    # Solution 2: 
        # Check: If s and t are not the same length, then not valid anagrams
        if len(s) != len(t):
            return False

        # Sort both strings and compare. If valid anagram, will return true 
        return sorted(s) == sorted(t)
        