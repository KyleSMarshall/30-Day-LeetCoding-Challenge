'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Ex:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''

# Solution

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        r = len(nums) - 1
        l = 0
        
        while l <= r:
            middle = (r + l) // 2
            if nums[middle] == target:
                return middle

            if (nums[middle] >= nums[0]) == (target >= nums[0]):
                # Normal BST
                if nums[middle] > target:
                    r = middle - 1
                else:
                    l = middle + 1
            
            elif nums[middle] >= nums[0] or target >= nums[0]:
                if nums[middle] > target:
                    l = middle + 1
                else:
                    r = middle - 1
        return -1
