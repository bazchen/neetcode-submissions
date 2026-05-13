class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 2: One Pass
        l = 0
        r = len(nums) - 1
        i = 0

        # Helper to swap elements at indices i and j
        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            # If element is 0, move to the left idx position. Increment left index. Increment i.
            if nums[i] == 0:
                swap(i,l)
                l += 1

            # If element is 2, swap to the right idx position. Decrement right index. DO NOT increment i.
            elif nums[i] == 2:
                swap(i,r)
                r -= 1
                i -= 1
            
            # Increment i if el was 0 or 1 (if 2, the code decrements i to cancel out effect)
            i += 1