'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Ex:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
'''

# Solution

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Create dict to store num of 0's and 1's up to that index
        d_min = {}
        d_max = {}
        num_0 = 0
        num_1 = 0
        for ind, val in enumerate(nums):
            
            if val == 0:
                num_0 += 1
            else:
                num_1 += 1
            
            diff = num_0 - num_1
            
            if diff not in d_min:
                d_min[diff] = ind
                
            if diff:
                d_max[diff] = ind - d_min[diff]
            else: 
                d_max[diff] = ind + 1
                
        if nums:
            return max(d_max.values())
        else:
            return 0
