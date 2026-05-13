class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1: Bucket Sort
        
        from collections import defaultdict
        # Iterate through nums and count freq of each element
        count=[0, 0, 0]
        for n in nums:
            count[n] += 1

        # Rewrite num with frequencies from 0 - 2
        idx = 0 
        for el in range(3):
            # write number at index, decrement count of that number, move to next index
            while count[el] > 0:
                nums[idx] = el
                count[el] -= 1
                idx += 1