class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution 2: Build Result, Prefix & Suffix Arrays (3 loops)

        # Create 3 Arrays: prefix, suffix and result - O(1)
        n = len(nums)
        prefix = [0] * n 
        suffix = [0] * n
        result = [0] * n

        # Set leftmost prefix value and rightmost suffix value = 1 (since at the bounds) - O(1)
        prefix[0] = 1
        suffix[n-1] = 1

        print(f"{nums=}, {n=}, {prefix=}, {suffix=}, {result=}")

        # Iterate forward through nums to fill prefix array - O(n)
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]

        print(f"{nums=}, {n=}, {prefix=}, {suffix=}, {result=}")

        # Iterate backwards through nums to fill suffix array - O(n)
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        # Build result array by computing prefix[i] * suffix[i] - O(n)
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        # Return result
        return result
