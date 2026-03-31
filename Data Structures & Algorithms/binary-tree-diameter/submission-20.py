# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#find the diameter between the length of any two nodes
#max(left_height, right_height)
#diameter doesn't have to pass through the root.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0


        def height(node):
            if not node:
                return 0

            l_height = height(node.left) 
            r_height = height(node.right)

            self.diameter = max(self.diameter, l_height + r_height)

            return max(l_height, r_height) + 1
        
        height(root)
        return self.diameter
