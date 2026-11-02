# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True
        if not p or not q :
            return False
        
        p1 = deque([p])
        q1 = deque([q])

        while p1 and q1 :
            node1 = p1.popleft()
            node2 = q1.popleft()

            if node1.val != node2.val :
                return False

            if node1.left and node2.left :
                p1.append(node1.left) 
                q1.append(node2.left) 
            elif node1.left or node2.left :
                return False
            
             
            if node1.right and node2.right :
                p1.append(node1.right) 
                q1.append(node2.right)
            elif node1.right or node2.right :
                return False
            
           
        return True 

        