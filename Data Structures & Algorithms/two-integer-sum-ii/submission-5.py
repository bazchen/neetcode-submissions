class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # Solution: 2 Pointers
        # Declare Left and Right Pointers
        l = 0
        r = 1
        length = len(numbers)

        # While pointers are not past the end
        while l < length-1:
            # if right pointer is at end of string, and no solution with current l. Shift pointers
            if r >= length:
                l += 1
                r = l + 1

            # elif num at l and r are same, not valid. increment r
            elif numbers[l] == numbers[r]:
                r += 1

            # elif l and r point to sum of target, solution found. Return l & r 1-indexed
            elif numbers[l] + numbers[r] == target:
                return [l+1, r+1]

            # elif l + r greater than target, then no need to check anymore r, so increment l & r
            elif numbers[l] + numbers[r] > target: 
                l += 1
                r = l + 1

            # elif l + r less than target, then increment r
            elif numbers[l] + numbers[r] < target: 
                r += 1

        # If loop finishes, then no solution found so return empty array
        return []
                

        