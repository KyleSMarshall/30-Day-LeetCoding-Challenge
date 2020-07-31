# Solution
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        '''
        Performs a binary search on the binaryMatrix columns. 
        We randomly check rows of the column in question by popping the values from the 'available' 
        set. This works because if we know in a certain column that rows 0, 1, and 2 do not contain 
        '1', but row 4 does, we do not need to consider rows 0, 1, 2 in our next binary search since 
        the rows are sorted in non-decreasing order.
        
        Keywork arguments:
        binaryMatrix: BinaryMatrix  --  An n*m binary matrix with rows sorted in non-decreasing order
        
        Returns:
        l: integer  --  The leftmost column that contains at least one '1', otherwise -1
        '''
        # Obtain the dimensions of the binary matrix
        [rows, cols] = binaryMatrix.dimensions()
        
        # Perform a binary search of the columns, randomly checking valid elements
        l, r = 0, cols
        
        # Create a set of available rows to seach for '1's
        available = set(range(rows))
        # Create an empty tried set
        tried = set()
        # Initialize last_valid_row to None 
        last_valid_row = None
        
        while l < r:
            
            # Calculate the middle column
            mid = l + (r - l) // 2

            while available:
                # Pop a random row from the available set
                row = available.pop()
                tried.add(row)
                
                # If we find a '1' somewhere in the column
                if binaryMatrix.get(row, mid) == 1:
                    
                    # Add back the row because it may still be valid
                    available.add(row)
                    # Reinitialize 'tried' as an empty set
                    tried = set()
                    # Update last row so that we know we have at least one valid column
                    last_valid_row = row
                    # Set the right bound to mid
                    r = mid
                    break
                    
            # If none of the rows had a 1
            else:
                # Need to add all the previously tried rows back to available since we will move to right
                available.update(tried)
                tried = set()
                # Set the left bound to mid + 1
                l = mid + 1
        
        # If we had at least one column that contained a '1'
        if last_valid_row is not None:
            return l
        return -1
        
