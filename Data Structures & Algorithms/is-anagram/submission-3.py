class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # # Solution 1: 
    #     # Early check: If s and t are not the same length, then not valid anagrams
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

    # # Solution 2: 
    #     # Early check: If s and t are not the same length, then not valid anagrams
    #     if len(s) != len(t):
    #         return False

    #     # Sort both strings and compare. If valid anagram, will return true 
    #     return sorted(s) == sorted(t)
        
    # Solution 3: Hash map
        from collections import defaultdict

        # Early check: If s and t are not the same length, then not valid anagrams
        if len(s) != len(t):
            return False
        
        # Determine n = length of s and t
        n = len(s)

        # Create empty dicts for counts of s and t
        countS, countT = defaultdict(int), defaultdict(int)

        # Iterate i from 0 to n
        for i in range(n):
            # increment count of letter s[i]
            countS[s[i]] += 1
            # increment count of letter s[i]
            countT[t[i]] += 1

        # If the two dicts match, then valid anagram and will return true. otherwise false.
        return countS == countT