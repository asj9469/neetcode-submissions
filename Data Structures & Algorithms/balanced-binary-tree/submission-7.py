# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        # compare depth of left and right
        def getDepth(root):
            if not root:
                return 0
            
            left = getDepth(root.left)
            right = getDepth(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(left-right) > 1:
                return -1

            return max(left, right) + 1

        return getDepth(root) != -1