class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import defaultdict

        mostFrequent = []
        count = defaultdict(int)

        # Count the frequency of each element in nums [O(n)]
        for num in nums:
            count[num] += 1

        # While k > 0 [O(k < n) ]
        while k > 0:
            # get key of element with max value. add el to mostFrequent list. change el's value to 0
            max_key, max_val = max(count.items(), key=lambda item: item[1])
            print(max_key)
            mostFrequent.append(max_key)
            count[max_key] = 0
            # decrement k
            k -= 1

        return mostFrequent