class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
    # # Solution 1: Using extend array method   
    #     # Create empty array ans
    #     ans = []

    #     # Extend ans by nums twice
    #     ans.extend(nums)
    #     ans.extend(nums)

    #     return ans


    # # Solution 2: Naive
    #     # Create empty array ans
    #     ans = []

    #     # Iterate  twice through nums and append to ans
    #     for _ in range(2):
    #         for num in nums:
    #             ans.append(num)

    #     return ans


    # Solution 3: Single pass
        # Determine n
        n = len(nums)

        # Create array ans of size 2n
        ans = [0] * (2*n)

        # Iterate through i, nums
        for i, num in enumerate(nums):
            ans[i] = num
            ans[i+n] = num

        return ans