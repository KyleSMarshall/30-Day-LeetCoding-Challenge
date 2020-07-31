 '''
 Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).
'''

# Solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1 for num in range(n)]
        right_prod = [1 for num in range(n)]
        result = [1 for num in range(n)]
        
        for i in range(n-1):
            left_prod[i + 1] = left_prod[i] * nums[i]
            right_prod[-i-2] = right_prod[-i-1] * nums[-i-1]
            
        for i in range(n):
            result[i] = right_prod[i] * left_prod[i]
            
        return result
