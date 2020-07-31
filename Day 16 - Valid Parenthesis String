'''
 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.

Ex:
Input: "(*))"
Output: True
'''

# Solution:

class Solution:
    def findMax(self, d, val, direction):
        res_max = None
        res_min = None
        for ind, value in enumerate(d):
            if value < val:
                res_max = ind
            else:
                res_min = ind
                break
                
        if direction == 'R':
            return res_max
        else:
            return res_min
    
    def checkValidString(self, s: str) -> bool:
        d = {'(': [], ')': [], '*': []}
        for ind, char in enumerate(list(s)):
            d[char].append(ind)
          
        while d['('] or d[')']:
            R, L, wild = None, None, None

            if d[')']:
                R = d[')'].pop(0)
            if d['(']:
                if R is not None:
                    ind = self.findMax(d['('], R, 'R')
                    if ind is not None:
                        L = d['('].pop(ind)
                else:
                    L = d['('].pop(0)
                
  
            if R is not None and L is not None:
                if R < L:
                    d[')'].append(R)
                    if d['*']:
                        wild = d['*'].pop(0)
                        if wild > R:
                            return False
                    else:
                        return False
                    
            elif R is not None and L is None:
                if d['*']:
                    ind = self.findMax(d['*'], R, 'R')
                    if ind is None:
                        return False
                    wild = d['*'].pop(ind)
                else:
                    return False
            
            elif L is not None and R is None:
                if d['*']:
                    ind = self.findMax(d['*'], L, 'L')
                    if ind is None:
                        return False
                    wild = d['*'].pop(ind)
                else:
                    return False
            
        return True       
