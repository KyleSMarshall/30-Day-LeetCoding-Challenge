# Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        
        
        def dfs(root, arr, depth):
            # Keep track of the level we're at in the tree.
            depth += 1

            if not root:
                return False, 0

            # -- Go left --
            valid_sequence, count = dfs(root.left, arr, depth)
            # If we have returned a match in the root val and arr
            if valid_sequence is True:
                count += 1
                # If we have a match, return 'True, count' and hop back up a level
                if root.val == arr[-count]:
                    return True, count
     
            # -- Go right --
            valid_sequence, count = dfs(root.right, arr, depth)
            # If we returned a match or we reached a leaf in the tree
            if valid_sequence is True or count == 0:
                if count == 0:
                    if depth != len(arr) or root.left:
                        return False, -1
                count += 1
                if root.val == arr[-count]:
                    return True, count

            # Default return
            return False, -1
        
        res = dfs(root, arr, 0)
        return res[0]
