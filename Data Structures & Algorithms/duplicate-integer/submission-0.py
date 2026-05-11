class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create seen array
        seen = []

        # Iterate through nums
        for n in nums:
            # If n has been seen, return true
            if n in seen:
                return True

            # else, add n to seen
            else:
                seen.append(n)
        
        # If we haven't early returned, return false
        return False

        