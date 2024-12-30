"""
1493. Longest Subarray of 1's After Deleting One Element: 
Return the size of the longest subarray containing only 1s 
after deleting one element.
"""
def longestSubarray(nums):
    left = 0             # Left pointer of the sliding window
    zeros = 0            # Counter for zeros in the current window
    max_len = 0          # Tracks the maximum length of a valid subarray

    for right in range(len(nums)):  # Expand the window by moving the right pointer
        if nums[right] == 0:
            zeros += 1  # Count the zero encountered in the window
        
        while zeros > 1:  # If more than one zero is in the window, shrink it
            if nums[left] == 0:
                zeros -= 1  # Decrement zero count if we move past a zero
            left += 1  # Shrink the window from the left
        
        # Calculate the maximum length (note: subtract one for the mandatory deletion)
        max_len = max(max_len, right - left)
    
    return max_len
