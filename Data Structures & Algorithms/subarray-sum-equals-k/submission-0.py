class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix Sum
        result = 0
        currentSum = 0 
        prefixSums = {0: 1}

        # Iterate through each num in nums and build the prefix sum array and result along the way
        for n in nums:
            # Track current sum so far and work out the difference to the target k
            currentSum += n
            diff = currentSum - k

            # Check if diff exists as a prefix, and if so increment the number of results
            result += prefixSums.get(diff, 0)

            # Update prefix sum array with the current total
            prefixSums[currentSum] = 1 + prefixSums.get(currentSum, 0)

        return result