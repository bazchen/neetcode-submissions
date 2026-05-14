class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Naive: Nested Loop that multiplies totals if not the same index

        totals = [1] * len(nums)
        # print(totals, len(totals))

        for idx, n in enumerate(nums):
            for j in range(len(totals)):
                # print("n=", n, "idx=", idx, "j=", j)
                if idx != j:
                    totals[j] *= n

        return totals
        