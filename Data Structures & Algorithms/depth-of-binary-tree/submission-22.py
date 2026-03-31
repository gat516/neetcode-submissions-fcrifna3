# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traversal(node):
            if not node:
                return 0
            left_depth = traversal(node.left)
            right_depth = traversal(node.right)

            return 1 + max(left_depth, right_depth)
        return traversal(root)
        