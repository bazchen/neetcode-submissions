class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Set pointer k which tracks open slot
        k = 0

        # Iterate through nums
        for i in range(len(nums)):
            # if the current num is not val, then move it to the open slot (position k). Increment k to next spot.
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k