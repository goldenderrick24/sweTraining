from heapq import heappush, heappop

def generateNewArray(arr, state, m):
    n = len(arr)
    res = []
    max_heap = []
    state = list(state)
    
    # Add all available elements to the max heap
    for i in range(n):
        if state[i] == '1':
            heappush(max_heap, (-arr[i], i))
    
    # Perform m operations
    for _ in range(m):
        # Get the maximum available value and its index
        while max_heap:
            max_val, max_idx = heappop(max_heap)
            max_val = -max_val
            if state[max_idx] == '1':  # Ensure the element is still available
                break
        else:
            break  # If no elements are available, stop

        # Append the maximum value to the result
        res.append(max_val)
        
        # Update state and push newly available elements into the heap
        for i in range(max_idx + 1):
            if state[i] == '0':
                state[i] = '1'
                heappush(max_heap, (-arr[i], i))
    
    return res

# Example usage
arr = [10, 5, 7, 6]
state = "0101"
m = 2
print(generateNewArray(arr, state, m))  # Output: [7, 10]
