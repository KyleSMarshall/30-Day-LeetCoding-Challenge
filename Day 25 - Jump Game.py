'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Ex:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''


# Solution:

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l, r = 0, nums[0]
        stop = len(nums) - 1
        while l <= r:
            r = max(r, l + nums[l])
            l += 1
            if r >= stop:
                return True
        return False
