from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    # Solution 1: Use Hash Map
        # Create Dictionary Count with num element as key and the count of each num as value
        counts = defaultdict(int)

        # Loop through array nums and increment count of element
        for n in nums:
            counts[n] += 1

        # Return key which has the maximum value (i.e. highest count), this is the majority element
        majorityEl = max(counts, key=counts.get)
        return majorityEl