'''
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the 
relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings 
is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Ex:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
'''

# Solution

class Solution:
    def __init__(self):
        self.memory = {}
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def DP(i, j):
            if i < 0 or j < 0:
                return 0   
            elif (i, j) in self.memory:
                return self.memory[(i,j)]
            else:
                if text1[i] == text2[j]:
                    self.memory[(i, j)] = DP(i - 1, j - 1) + 1
                else:
                    self.memory[(i, j)] = max(DP(i, j - 1), DP(i - 1, j))
            return self.memory[(i,j)]
        
        return DP(len(text1)-1, len(text2)-1)
            
