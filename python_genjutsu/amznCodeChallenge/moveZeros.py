def moveZeros(arr):
    nonZeroPos = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[nonZeroPos] = arr[i]
            nonZeroPos += 1
    
    for i in range(nonZeroPos, len(arr)):
        arr[i] = 0