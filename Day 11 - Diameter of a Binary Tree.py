'''
 Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Ex:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them. 
'''

# Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root:
            self.nodeStart(root)
            self.helper(root)
        else:
            return 0
        #print(self.sizes)
        return self.max
        
    def helper(self, root):
        if root.left:
            nodeL = root.left
            self.nodeStart(nodeL)
            self.helper(nodeL)
        if root.right:
            nodeR = root.right
            self.nodeStart(nodeR)
            self.helper(nodeR)
            
        
    def nodeStart(self, root):
        if root.left:
            l = self.longest(root.left)
        else:
            l = 0
        if root.right:
            r = self.longest(root.right)
        else:
            r = 0
        self.max = max(self.max, l + r)

    def longest(self, root: TreeNode):
        
        if root is None:
            return 0
        
        lheight = self.longest(root.left)
        rheight = self.longest(root.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
        
        
