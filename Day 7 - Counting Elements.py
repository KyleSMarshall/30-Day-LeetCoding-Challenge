# Problem
'''
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

Example - 
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
'''

# Solution: O(n) time complexity
class Solution:
    def countElements(self, arr: List[int]) -> int:
    '''
    Counts the number of elements x such that x + 1 is also in arr by utilizing hashmaps.
    
    Keyword arguments:
    arr: List - The input list of integers
    
    Returns:
    res: Int - Returns an integer for the sum of valid elements x such that x + 1 was in arr.
    '''
        # Place the list of numbers in a dictionary
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        # Initialize the output result to 0
        res = 0
        
        # Loop through the keys and count the valid values
        for key in d.keys():
            if key + 1 in d:
                res += d[key]
        
        return res
        
