"""
643. Maximum Average Subarray I: You are given an integer array nums 
consisting of n elements, and an integer k. 
Find a contiguous subarray whose length is equal to k that has
the maximum average value and return this value.


- Calculate the sum of the first k elements to create the initial window sum.
- Slide the window by adding the next element and subtracting the 
  first element of the current window.
- Update the maximum average at each step.

"""

def findmaxAvg(nums,k):
    windowSum = sum(nums[:k])
    maxAvg = windowSum / k
    for i in range(k,len(nums)):
        windowSum += nums[i] - nums[i-k]
        maxAvg = max(maxAvg, windowSum/k)
    
    return maxAvg   
