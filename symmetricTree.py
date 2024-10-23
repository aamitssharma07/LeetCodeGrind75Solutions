# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetry(p,q):
            if(p==None and q == None):
                return True
            elif(p==None or q==None or p.val!=q.val):
                return False
            else:
                left_right = checkSymmetry(p.left,q.right)
                right_left =   checkSymmetry(p.right,q.left)   
                return   left_right and right_left     
            return True
        if(root.left is None  and root.right is None):
            return True
        else:
            return checkSymmetry(root.left,root.right)