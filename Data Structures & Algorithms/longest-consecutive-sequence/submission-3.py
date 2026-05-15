class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Variables for current and longest sequences
        currentSeq = []
        longestSeq = []

        # Sort nums and store as set to remove duplicates
        nums = sorted(set(nums))

        # Iterate through sorted nums
        for num in nums:
            # If current sequence is empty, add num
            # print(nums, num, currentSeq, longestSeq)
            if len(currentSeq) == 0:
                currentSeq.append(num)

            # If num is consecutive value (i.e. last value in var + 1), append num
            elif (num == currentSeq[-1] + 1):
                currentSeq.append(num)

            # If num is not (last value in var + 1)
            else:
                # If current longer than longest, update longest
                if len(currentSeq) > len(longestSeq):
                    longestSeq = currentSeq

                # Restart current sequence to be only current num
                currentSeq = [num]

        # If current longer than longest, update longest
        if len(currentSeq) > len(longestSeq):
            longestSeq = currentSeq

        return len(longestSeq)