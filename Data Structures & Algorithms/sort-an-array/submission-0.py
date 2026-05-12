class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    # Solution 1: Merge Sort (Divide & Conquer)

        # Merges left and right halves of array
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            # Pointers: i points to array index, j for left and k for right
            i, j, k = L, 0, 0

            # while both pointers are in bounds (i.e. values remain in both subarrays), compare and add smallest value
            while j < len(left) and k < len(right):
                # If left value is smaller or equal to right, then insert right value to array at i
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                # If right value is smaller, then insert at i and increment right k index
                else:
                    arr[i] = right[k]
                    k += 1
                # Increment the array pointer position everytime
                i += 1
            
            # while values remain in left subarray, then keep adding those values to parent array
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            # while values remain in right subarray, then keep adding those values to parent array 
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1


        def mergeSort(arr, l, r):
            # Base Case:
            if l >= r:
                return

            # Determine midpoint of array
            m = (l + r) // 2

            # Recursively call on left and right halves
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)

            # Then merge subarrays
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums

