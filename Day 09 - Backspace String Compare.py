'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Ex:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
'''

# Solution

class Solution:
    
    def inPlaceModifier(self, string):
        string = list(string)
        slow = 0
        fast = 0
        
        while fast < len(string):
            print(slow, fast)
            if string[fast] != '#':
                string[fast], string[slow] = '', string[fast]
                slow += 1
            elif slow >= 0:
                slow = max(0, slow-1)
                string[slow], string[fast] = '', ''
            fast += 1
        string = ''.join(string)
        return string
        
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.inPlaceModifier(S) == self.inPlaceModifier(T)
