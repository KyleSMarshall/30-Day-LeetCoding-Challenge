# Problem
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the 
number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example - 
Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

# Solution: (Faster than 88.04% of Python3 solutions)
class Solution:

    def __init__(self):
        self.history = []
        
    def isHappy(self, n: int, history = [], happy = [], sad = []) -> bool:            
        '''
        Computes if a number is happy by recursively splitting the number into single 
        digit integers and summing the integers' squares.
        Keeps a history of previously computed happy and sad numbers to avoid redundant calculations.
        
        Keyword arguments:
        n - integer: number to be determined if happy or sad
        history - array: local history of numbers that were seen in the calculation
        happy - array: running history of previously encountered happy numbers
        sad - array: running history of preiouvsly encounted sad numbers
        '''
        
        if n in happy:
            return True
        elif n in sad:
            return False
        
        if n == 1:
            happy += self.history
            return True
        
        self.history.append(n)
        n = str(n)
        n = sum([int(dig)**2 for dig in n])
        
        if n not in history:
            return self.isHappy(n, self.history, happy, sad)
        else:
            sad += self.history
            return False
