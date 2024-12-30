724. Find Pivot Index
Table 1: Problem Analysis
Data Structure	Logic Steps	Code Example	Algorithm	Key Words
Array (Prefix Sum)	- Calculate the total sum of the array.
- Iterate through the array while maintaining the left sum.
- For each index, check if left sum == right sum.	def pivotIndex(nums):\n total_sum = sum(nums)\n left_sum = 0\n for i, num in enumerate(nums):\n if left_sum == total_sum - left_sum - num:\n return i\n left_sum += num\n return -1	Prefix Sum	"pivot index", "left sum", "right sum", "balanced index"
