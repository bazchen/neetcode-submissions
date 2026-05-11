class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create seen hash set
        seen = set()

        # Iterate through nums
        for n in nums:
            # If n has been seen, return true
            if n in seen:
                return True

            # else, add n to seen
            else:
                seen.add(n)
        
        # If we haven't early returned, return false
        return False

        