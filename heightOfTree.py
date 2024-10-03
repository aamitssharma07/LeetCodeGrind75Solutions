# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #function for calculating the height 

        def Height(root):
            if(not root.left and not root.right): #This condition checks node leaf
                return 1
            else:
                if(not root.left): #This condition checks that left is nulll 
                    return 1 + Height(root.right)
                elif(not root.right):
                    return 1 + Height(root.left)#This condition checks that left is nulll 
                else:
                    return 1 + max(Height(root.right),Height(root.left))

        if(not root):
            return 0
        else:
            return Height(root) 