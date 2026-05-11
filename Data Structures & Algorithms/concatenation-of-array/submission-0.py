class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
    # Solution 1: Using extend array method   
        # Create empty array ans
        ans = []

        # Extend ans by nums twice
        ans.extend(nums)
        ans.extend(nums)

        return ans

    # # Solution 2: Naive
    #     # Calculate n = length of nums
    #     n = len(nums)

    #     # Create empty array ans
    #     ans = []

    #     # Iterate i through 0 to n-1 and set ans[i] = num[i] twice
    #     for i in range(n):
    #         ans.append(nums[i])

    #     for i in range(n):
    #         ans.append(nums[i])

    #     return ans