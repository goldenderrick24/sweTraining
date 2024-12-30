from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    for i in range(len(unsorted_list)):
        current = i
        # gets the smallest element and inserts it at current index
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            # swaps current smaller element with the element before it
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1]\
                , unsorted_list[current]
            current -= 1
    return unsorted_list

def selection_sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        # Assume the current position as minimum
        min_index = i

        # Find the minimum element's index from the rest of the list
        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j

        # Swap the minimum element with the first element
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index],\
            unsorted_list[i]
    return unsorted_list

def bubble_sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)

    # Iterate through all list elements in reversed order
    for i in reversed(range(n)):
        # Track whether a swap occurred in this pass
        swapped = False
        for j in range(i):
            # Swap if the element found is greater than the next element
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], \
                    unsorted_list[j]
                swapped = True

        # If no two elements were swapped, the list is sorted
        if not swapped:
            return unsorted_list
    return unsorted_list


def merge_sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)

    # Base case: A list of size 1 or 0 is already sorted
    if n <= 1:
        return unsorted_list

    # Split the list into left and right halves
    midpoint = n // 2
    left_list = sort_list(unsorted_list[:midpoint])
    right_list = sort_list(unsorted_list[midpoint:])

    result_list = []
    left_pointer, right_pointer = 0, 0

    # Merge the sorted left and right lists with two pointers
    while left_pointer < midpoint or right_pointer < n - midpoint:
        if left_pointer == midpoint:
            # If left list is empty, append element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint:
            # If right list is empty, append element from left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]:
            # Append smaller element from left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:  # Append smaller element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1

    return result_list

def sort_list_interval(unsorted_list: List[int], start: int, end: int) -> None:
    # If segment is 1 or 0, it's sorted
    if end - start <= 1:
        return

    # Using last element as the pivot
    pivot = unsorted_list[end - 1]
    start_ptr, end_ptr = start, end - 1

    # Partitioning process
    while start_ptr < end_ptr:
        # Find the next element from the left that is larger than the pivot
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1

        # Find the next element from the right that is smaller than or equal to the pivot
        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1

        # Swap if pointers haven't met
        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]

    # Place pivot in its final position
    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]

    # Sort left and right of the pivot
    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)

def sort_list(unsorted_list: List[int]) -> List[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
    return unsorted_list