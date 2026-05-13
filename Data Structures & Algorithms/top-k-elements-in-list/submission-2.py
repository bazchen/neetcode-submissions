class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Solution 3: Bucket Sort using index of array to represent frequency [O(n)]
        count = {}
        freq = [[] for i in range(len(nums) +1)]

        # Create Hash map with count of each element
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # The index of the freq array represents the frequency of the elements in that position
        for n, c in count.items():
            freq[c].append(n)

        # Loop through frequency array from highest frequency (rightmost index). Append el to result. 
        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
