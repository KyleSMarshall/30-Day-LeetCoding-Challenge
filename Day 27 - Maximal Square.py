'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Ex:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

# Solution

class Solution:
    def maximalSquare(self, matrix):
        # Make a history of viewed indices
        # Let's try a good ol' BFS approach
        
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        squares = 0
        for col in range(cols):
            if max_area >= (cols - col)**2:
                break
            for row in range(rows):
                
                if matrix[row][col] == '1':
                    temp_row, temp_col = row, col

                    length = 1
                    height = 0
                    while matrix[temp_row][temp_col] == '1':
                        if temp_row == rows - 1 or temp_col == cols - 1:
                            temp_row += 1
                            break
                        temp_row += 1

                    if (temp_row - row) ** 2 > max_area:

                        j = col
                        max_length = temp_row - row
                        while j < col + max_length and j < cols:
                            length = 0
                            height += 1

                            for i in range(row, temp_row):
                                if matrix[i][j] == '0':
                                    cont = False
                                    break
                                else:
                                    length += 1

                            max_length = min(max_length, length)

                            if length >= height:
                                max_area = max(max_area, height**2)
                            if length < height:
                                break
                            j += 1
                        #max_area = max(max_area, min(height,length)**2)
                            
        return max_area
