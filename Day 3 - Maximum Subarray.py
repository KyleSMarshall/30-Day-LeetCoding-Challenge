# Problem:
'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example - 
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# Solution: (Faster than* 68.13% of Python3 solutions)
# *My solution runs in O(n) time which is the same as the top ~70% of sumbmissions and so there is
# is great variability in the run-time of the code. I fall between the top 8% and 41% when running
# the same code multiple times.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        running_sum = 0
        
        for i in range(len(nums)):

            if (-1*nums[i]) > running_sum:
                running_sum = 0
            else:
                running_sum += nums[i]
                max_sum = max(max_sum, running_sum)
        
        return max_sum
