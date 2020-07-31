'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Ex:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

# Solution

class Solution:
    
    def __init__(self):
        # Keep a dict showing the minimum path from an index onward
        self.min_path = {}
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid:
            m = len(grid)
            n = len(grid[0])
        else:
            return 0
        
        self.helper(grid, (0,0), m, n)
        return self.min_path[(0,0)]
        
        
    def helper(self, grid, ind, rows, cols):
        # Check in ind are already in the cache
        if ind in self.min_path:
            return self.min_path[ind]

        if ind == (rows-1, cols-1):
            self.min_path[ind] = grid[ind[0]][ind[1]]
            return self.min_path[ind]

        if ind[0] == rows-1:
            self.min_path[ind] = grid[ind[0]][ind[1]] + self.helper(grid, (ind[0], ind[1] + 1), rows=rows, cols=cols)
            return self.min_path[ind]
        if ind[1] == cols-1:
            self.min_path[ind] = grid[ind[0]][ind[1]] + self.helper(grid, (ind[0] + 1, ind[1]), rows=rows, cols=cols)
            return self.min_path[ind]
        self.min_path[ind] = grid[ind[0]][ind[1]] + min(self.helper(grid, (ind[0] + 1, ind[1]), rows=rows, cols=cols), self.helper(grid, (ind[0], ind[1] + 1), rows=rows, cols=cols))

        return self.min_path[ind]
        
        
