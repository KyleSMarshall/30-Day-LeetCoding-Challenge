'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree 
along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Ex:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

# Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        '''
        Finds the maximum path through a binary tree.
        Start at the root node and keep a running total of the maximum path left and right (independent of
        the root node). If the we reach the bottom, begin trying alternate paths up to the top.
        We need to calculate the maximum left and right paths from a root node so that we can reuse it when
        trying higher up roots. 
        
        What if we create another binary tree containing the maximum left and right values? 
        '''
        
        # Use DFS
        def DFS(root):
            if not root:
                return 0, -float('inf')
            
            left_max, sum_left = DFS(root.left)
            right_max, sum_right = DFS(root.right)

            if left_max < 0:
                left_max = root.val
            else:
                left_max += root.val
                
            if right_max < 0:
                right_max = root.val
            else:
                right_max += root.val
                
            maximum = left_max + right_max - root.val
            return max(left_max, right_max), max(maximum, sum_left, sum_right)
        
        max_sum = DFS(root)[1]
        return max_sum if max_sum != -float('inf') else 0
