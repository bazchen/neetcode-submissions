class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

    # # Solution 1: Brute Force
    #     # Iterate through i in nums
    #     n = len(nums)
    #     for i in range(n):
    #         # iterate through j in rest of nums
    #         for j in range(i+1, n):
    #             # if sum of two numbers equals target, then return indexes
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]


    # Solution 2: Hash Map
        # Create seen dictionary
        seen = {}

        # Iterate through each value in nums
        for i, n in enumerate(nums):
            # Calculate difference between target and current n
            diff = target - n

            # If diff has already been seen, then index pair found so return
            if diff in seen:
                return [seen[diff], i]

            # Otherwise, add key n with value of index i to seen
            seen[n] = i

        # If loop finishes with no match, return empty array
        return []
        