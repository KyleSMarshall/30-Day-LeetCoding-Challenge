# Problem
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
'''

# Solution: (Fatser than 80.32% of Python3 solutions)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Stores the used numbers in a set. If the number is not already in the set we add the number to
        the running sum, if it is in the set we subtract it.
        '''
        total = 0
        used = set()
        for num in nums:
            if num not in used:
                total += num
                used.add(num)
            else:
                total -= num

        return total
