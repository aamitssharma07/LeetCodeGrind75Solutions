# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverse(root):
            if(root==None):
                return
            else:

                if(root.left!=None or root.right!=None): #This condition is to check that if it's not a leaf then only perform below steps

                    if(root.left==None):#This will check that only right node is there
                        inverse(root.right)
                        root.left = root.right
                        root.right = None
                    elif(root.right==None):#This will check that only rleft ght node is there
                        inverse(root.left)
                        root.right = root.left
                        root.left = None
                    else:
                        inverse(root.left)
                        inverse(root.right)
                        temp = root.right
                        root.right = root.left
                        root.left = temp

        inverse(root)
        return root


#TimeComplexity and space complexity if O(n) 