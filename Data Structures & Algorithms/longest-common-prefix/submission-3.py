class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    # Solution 1: Lexographically sort strings and then compare first and last strings 
        # Sort strs in alphabetical
        sortedStrings = sorted(strs)

        # Declare empty prefix string var and get first and last strings
        prefix = ''
        first = sortedStrings[0]
        last = sortedStrings[-1]

        # Get char at index i of first word of the sorted strings
        for i, char in enumerate(first):

            # If there is a mismatch between the chars at this index, terminate and return
            if char != last[i]:
                return prefix

            # If chars match, append char to prefix
            prefix += char

        # return prefix
        return prefix
            