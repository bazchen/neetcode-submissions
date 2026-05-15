class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # Solution 2: Using Hash Set
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Check if it is the beginning of a potential sequence by seeing if num-1 exists
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest
