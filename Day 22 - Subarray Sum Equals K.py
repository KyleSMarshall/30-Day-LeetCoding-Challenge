'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Ex:

Input:nums = [1,1,1], k = 2
Output: 2
'''

# Solution

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums = {nums[0]: [0]}
        running_sum = nums[0]
        for i in range(1, len(nums)):
            running_sum += nums[i]
            if running_sum in sums:
                sums[running_sum].append(i)
            else:
                sums[running_sum] = [i]
        
        ans = 0
        for sum_ in sums.keys():
            if sum_ == k:
                if k == 0:
                    # 0 is a special case where we have n(n-1)/2 combinations 
                    ans += int(len(sums[sum_]) * (len(sums[sum_]) + 1) / 2)
                else:
                    ans += len(sums[sum_])
                    
            elif sum_ - k in sums:
                # We have another key which adds up to the target. Now we need to see if the indices work
                for ind in sums[sum_]:
                    ans += len([x for x in sums[sum_ - k] if x < ind])
        return ans                
        
        
