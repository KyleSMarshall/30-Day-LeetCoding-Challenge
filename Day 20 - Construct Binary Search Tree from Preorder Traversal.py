'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Ex:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
'''

# Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        tree = TreeNode(preorder[0])
        
        def helper(preorder, tree, num):
            if num < tree.val:
                if tree.left:
                    return helper(preorder, tree.left, num)
                else:
                    tree.left = TreeNode(num)
            else:
                if tree.right:
                    return helper(preorder, tree.right, num)
                else:
                    tree.right = TreeNode(num)
            
        for num in preorder[1:]:
            helper(preorder, tree, num)
            
        return tree
