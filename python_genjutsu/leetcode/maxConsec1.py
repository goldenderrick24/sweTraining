"""

1004. Max Consecutive Ones III: Given a binary array nums 
and an integer k, return the maximum number of consecutive 1s 
if you can flip at most k zeros.
Use a sliding window to track the longest subarray of 1s 
that can be formed by flipping at most k zeros. 
Adjust the left pointer when the number of zeros exceeds k.

- Use a sliding window.
- Track the number of zeros in the current window.
- If zeros exceed k, shrink the window.



In this context, "flip" means to temporarily change the 

value of a 0 in the binary array nums to 1. 
This allows you to count it as part of a sequence 
of consecutive 1s. However, this flip is hypothetical—
no actual changes are made to the array. 
Instead, the algorithm assumes the ability to 
"flip" up to k zeros and tracks how many 
flips have been "used" with the k counter.

For example:

If nums = [1, 0, 1, 0, 1] and k = 1:

Think of k as "lives" in a video game:

Encounter a 0 (hit an obstacle):

You "spend" one life (k -= 1) to flip that 0 
into a 1 and continue your sequence.
Run out of lives (k < 0):

You can no longer flip any zeros, so you must 
"retreat" by shrinking the sequence from the left (left += 1) 
until you regain a life (k >= 0).
Count the sequence when valid:

While you still have lives (or have made the sequence valid again 
by shrinking), you can calculate the length of the current sequence of 1s.
Maximize the streak:

The algorithm continuously tracks the largest sequence possible 
while using your limited "lives" wisely.
This perspective emphasizes how the sliding window dynamically 
adjusts based on the available "lives" (flips). It's all about m
aking the most out of your limited resources (flips) to achieve 
the longest streak of consecutive 1s!
"""

def longone(nums,k):
    l = 0
    for r in range(len(nums)): # Right pointer iterates through the array
        if nums[r] == 0:
            k-=1 # Decrease `k` for every 0 encountered
        if k < 0:
            if nums[l] == 0:
                k +=1 # Restore `k` if we slide past a 0
            l+=1 # Shrink the window from the left
        return r - l + 1  # The size of the window is the maximum length
