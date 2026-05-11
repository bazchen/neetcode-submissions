class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    # # Solution 1: Lexographically sort strings and then compare first and last strings 
    #     # Sort strs in alphabetical
    #     sortedStrings = sorted(strs)

    #     # Declare empty prefix string var and get first and last strings
    #     prefix = ''
    #     first = sortedStrings[0]
    #     last = sortedStrings[-1]

    #     # Get char at index i of first word of the sorted strings
    #     for i, char in enumerate(first):

    #         # If there is a mismatch between the chars at this index, terminate and return
    #         if char != last[i]:
    #             return prefix

    #         # If chars match, append char to prefix
    #         prefix += char

    #     # return prefix
    #     return prefix

    # Solution 2: Assume first word is prefix
        # Assume first word is common prefix
        prefix = strs[0]

        # Loop through remaining words
        for word in strs[1:]:

            # While current word does not start with our prefix
            while not word.startswith(prefix):
                # Remove last letter off the prefix and check again
                prefix = prefix[:-1]

                # If prefix is now empty, then no common prefix
                if prefix == '':
                    return ''

        # What remains will be the longest remaining prefix. Return prefix
        return prefix
            