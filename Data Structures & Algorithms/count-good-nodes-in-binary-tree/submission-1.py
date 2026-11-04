# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root , root.val)])
        cnt = 0

        while q  :
            node, a = q.popleft()

            if node.val >= a :
                cnt += 1
            
            a = max( a , node.val)
            
            if node.left :
                q.append((node.left ,a))
            
            if node.right :
                q.append((node.right ,a))
        
        return cnt
        