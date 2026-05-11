class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # declare empty prefix string var
        prefix = ''

        # Sort strs in alphabetical
        sortedStrings = sorted(strs)

        # Get char at index i of first word of the sorted strings
        for i, char in enumerate(sortedStrings[0]):
            # Go through each other word in strs
            for word in sortedStrings[1:]:
                
                # If there is a mismatch between the chars at this index, terminate loop
                if char != word[i]:
                    return prefix

            # If matches all, append char to prefix
            prefix += char

        # return prefix
        return prefix
            
        