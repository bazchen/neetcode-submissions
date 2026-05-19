class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Solution: Two Pointers
        # Declare Left and Right Pointer
        l, r = 0, len(s) - 1

        # Keep comparing until pointers meet in middle/cross
        while l < r: 
            # While not alphanum, increment / decrement pointers
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # compare lower case chars at pointer position
            if s[l].lower() != s[r].lower():
                return False

            # Move pointer
            l, r = l + 1, r - 1
        
        return True

    # Helper: use ascii values to determine if alphanumerical
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
