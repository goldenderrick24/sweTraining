# Recursive binary search function
def rec_binary_search(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2

        # Element is present at the middle
        if arr[mid] == x:
            return mid

        # Element is smaller than mid, search left subarray
        if arr[mid] > x:
            return rec_binary_search(arr, low, mid - 1, x)

        # Else search right subarray
        return rec_binary_search(arr, mid + 1, high, x)

    return -1

# Binary search function
def binary_search(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Merge Sort
def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Utility function to print array
def print_array(arr):
    print(" ".join(map(str, arr)))

# Driver code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    query = 10
    n = len(arr)

    # Binary Search
    result = binary_search(arr, 0, n - 1, query)
    if result == -1:
        print("Element is not present in array")
    else:
        print(f"Element is present at index {result}")

    # Sorting examples
    arr_to_sort = [64, 34, 25, 12, 22, 11, 90]
    print("\nOriginal Array:")
    print_array(arr_to_sort)

    # Selection Sort
    selection_sort(arr_to_sort)
    print("\nSorted with Selection Sort:")
    print_array(arr_to_sort)

    # Quick Sort
    arr_to_sort = [64, 34, 25, 12, 22, 11, 90]
    quick_sort(arr_to_sort, 0, len(arr_to_sort) - 1)
    print("\nSorted with Quick Sort:")
    print_array(arr_to_sort)

    # Merge Sort
    arr_to_sort = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(arr_to_sort, 0, len(arr_to_sort) - 1)
    print("\nSorted with Merge Sort:")
    print_array(arr_to_sort)
