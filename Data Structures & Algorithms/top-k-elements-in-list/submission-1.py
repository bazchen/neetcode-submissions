class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Solution 2: Using Heaps
        import heapq
        from collections import Counter

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)