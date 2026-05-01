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

        def getMaxDepth(node) -> int:
            if not node:
                return 0
            
            return 1 + max(getMaxDepth(node.left), getMaxDepth(node.right))

        def checkBalance(node) -> bool:
            print(abs(getMaxDepth(node.left) - getMaxDepth(node.right)))
            return abs(getMaxDepth(node.left) - getMaxDepth(node.right)) <= 1

        if checkBalance(root):
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
        
        

        
        