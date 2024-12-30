class Solution:
   """
   You are given an integer array nums and an integer k.

    In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

    Return the maximum number of operations you can perform on the array.
   
   """
   
def maxOperations(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array using Quicksort
        def quicksort(arr, low, high):
            if low < high:
                pivot_index = partition(arr, low, high)
                quicksort(arr, low, pivot_index - 1)
                quicksort(arr, pivot_index + 1, high)

        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        quicksort(nums, 0, len(nums) - 1)  # Sort the array in-place

        # Step 2: Use Two-Pointer Technique
        i, j = 0, len(nums) - 1
        max_operations = 0

        while i < j:
            current_sum = nums[i] + nums[j]
            if current_sum == k:
                # Found a valid pair
                max_operations += 1
                i += 1
                j -= 1
            elif current_sum < k:
                # Sum is too small, move the left pointer
                i += 1
            else:
                # Sum is too large, move the right pointer
                j -= 1

        return max_operations
