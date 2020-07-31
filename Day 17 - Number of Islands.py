'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Ex:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
'''

# Solution

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Use a type of BFS approach
        if not grid:
            return 0
        
        # Make a set of the indices to try
        ones_list = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    ones_list.add((row, col))
        
        def check_surrounding(grid, ind, visited, H = len(grid), L = len(grid[0])):
            next_inds = set()
            
            if H > 1:
                # Do vertical touching
                if ind[0] == 0:
                    new_ind = (1, ind[1])
                    if grid[new_ind[0]][new_ind[1]] == "1" and new_ind in ones_list:
                        next_inds.add(new_ind)
                elif ind[0] == H - 1:
                    new_ind = (ind[0]-1, ind[1])
                    if grid[new_ind[0]][new_ind[1]] == "1" and new_ind in ones_list:
                        next_inds.add(new_ind)
                else:
                    new_ind = (ind[0]+1, ind[1])
                    if grid[new_ind[0]][new_ind[1]] == "1" and new_ind in ones_list:
                        next_inds.add(new_ind)
                    new_ind = (ind[0]-1, ind[1])
                    if grid[new_ind[0]][new_ind[1]] == "1" and new_ind in ones_list:
                        next_inds.add(new_ind)
            
            if L > 1:
                # Horizontal touching
                if ind[1] == 0:
                    new_ind = (ind[0], 1)
                    if grid[new_ind[0]][new_ind[1]] == "1" and new_ind in ones_list:
                        next_inds.add(new_ind)
                elif ind[1] == L - 1:
                    new_ind = (ind[0], ind[1] - 1)
                    if grid[new_ind[0]][new_ind[1]] == "1" and new_ind in ones_list:
                        next_inds.add(new_ind)
                else:
                    new_ind = (ind[0], ind[1] - 1)
                    if grid[new_ind[0]][new_ind[1]] == "1" and new_ind in ones_list:
                        next_inds.add(new_ind)
                    new_ind = (ind[0], ind[1] + 1)
                    if grid[new_ind[0]][new_ind[1]] == "1" and new_ind in ones_list:
                        next_inds.add(new_ind)
        
            return next_inds
                
        def BFS(grid, ones_list):
            islands = 0
            while ones_list:
                val = (ones_list.pop())
                queue = set()
                queue.add(val)
                ones_list.add(val)
                while queue:
                    current = queue.pop()
                    ones_list.remove(current)
                    queue.update(check_surrounding(grid, current, ones_list))
                islands += 1
            return islands
        
        return BFS(grid, ones_list)
