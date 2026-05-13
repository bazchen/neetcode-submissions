class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ''

        # Iterate through list of strings
        for s in strs:
            # Add string to encodedString (lenght#string)
            encodedString += str(len(s)) + '#' + s

        print(encodedString)
        return encodedString

    def decode(self, s: str) -> List[str]:
        startIdx = 0
        decodedStrings = []

        # Iterate through array of string lengths
        while startIdx < len(s):
            # Slice all characters up to the # for the word length
            j = startIdx
            while s[j] != '#':
                j += 1
            length = int(s[startIdx:j])

            # Skip next char # and then slice the length determined. Add sliced word to decodedStrings
            decodedStrings.append(s[j+1:j+1+length])

            # Move pointer by length
            startIdx = j+1+length
        
        return decodedStrings
