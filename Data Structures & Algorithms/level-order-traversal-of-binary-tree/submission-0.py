# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue, output = deque(), []
        queue.append(root)

        # queue = [4, 5, 6, 7]
        # [1], [2, 3], []
        # node = 2
        while queue:
            newList = []
            
            for i in range(len(queue)):
                node = queue.popleft()
                newList.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            output.append(newList)
        return output