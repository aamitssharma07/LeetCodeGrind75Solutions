# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#*****************Optimized LCA***********************************
        def LCA(root,p,q):
            if((p.val > root.val and q.val< root.val) or (p.val < root.val and q.val> root.val)):
                return root
            elif(p.val == root.val):
                return root
            elif(q.val == root.val):
                return root
            else:
                if(p.val>root.val):
                    return LCA(root.right,p,q)
                else:
                    return LCA(root.left,p,q)