class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Variables
        counts = defaultdict(int)
        results = []
        n = len(nums)

        # Loop through nums and count - O(n)
        for num in nums:
            counts[num] += 1

        # Loop through counts - O(n)
        for key, value in counts.items():
            # If value is greater than n then add to results array
            if value > n/3:
                results.append(key)

        # Return results
        return results
            