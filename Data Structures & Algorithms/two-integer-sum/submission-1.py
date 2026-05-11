class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through i in nums
        n = len(nums)
        for i in range(n):
            # iterate through j in rest of nums
            for j in range(i+1, n):
                # if sum of two numbers equals target, then return indexes
                if nums[i] + nums[j] == target:
                    return [i, j]
        