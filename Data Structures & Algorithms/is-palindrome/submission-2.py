class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert string into array with removed non-alphanumberical chars and all lowercase - O(n)
        cleanedS = []
        for char in s:
            if char.isalnum():
                cleanedS.append(char.lower())
        
        # Edge case: if cleaned S is empty, then is a palidrome

        if len(cleanedS) == 0:
            return True

        # Determine midpoint index which is the floor of midway
        midpointIndex = len(cleanedS)//2

        # Iterate through the string
        for i in range(len(cleanedS)):
            # If it is the middle char, then palindrome. return true
            if i == midpointIndex:
                return True

            # Compare char with opposing char with negative index. If not equal, return false
            elif cleanedS[i] != cleanedS[-i-1]:
                return False
