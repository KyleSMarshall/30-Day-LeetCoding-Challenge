'''
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Ex:
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
'''

# Solution

import bisect

class Solution:
    
    def helper(self, stones, length):
        if length > 1:
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            new_stone = stone_1 - stone_2
            if new_stone:
                bisect.insort(stones, new_stone)
                length -= 1
            else:
                length -= 2
            return self.helper(stones, length)
        
        elif length == 1:
            return stones[0]
        
        else:
            return 0
        
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        length = len(stones)
        return self.helper(stones, length)
        
        
