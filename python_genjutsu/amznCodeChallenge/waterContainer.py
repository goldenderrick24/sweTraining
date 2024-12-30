from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = 0  # To keep track of the largest area
        
        # Loop until the two pointers meet
        while i <= j:
            # Calculate the current area
            currArea = (j - i) * min(height[i], height[j])
            
            # Update maxArea if the current area is larger
            maxArea = max(maxArea, currArea)
            
            # Move the pointer corresponding to the shorter line
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return maxArea
auth_url