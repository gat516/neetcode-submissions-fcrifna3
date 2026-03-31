# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        upperBound = float('inf')
        lowerBound = float('-inf')

        def traversal(node, lower, maximum):
            if node == None:
                return True
            if node.val >= maximum or node.val <= lower:
                return False

            return traversal(node.left, lower, node.val) and traversal(node.right, node.val, maximum)
        
        return traversal(root, lowerBound, upperBound)