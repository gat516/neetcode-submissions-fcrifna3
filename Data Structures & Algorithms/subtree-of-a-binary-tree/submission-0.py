# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(mainRoot, subRoot):
            if not mainRoot and not subRoot:
                return True
            if not mainRoot or not subRoot:
                return False
            if mainRoot.val != subRoot.val:
                return False
            return sameTree(mainRoot.left, subRoot.left) and sameTree(mainRoot.right, subRoot.right)

        if not root:
            return False
        if root.val == subRoot.val:
            if sameTree(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
        