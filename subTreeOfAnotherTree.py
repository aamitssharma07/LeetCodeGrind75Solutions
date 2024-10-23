# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findSubRootNodes(root):
            subRootNodes = []
            if(root == None):
                return subRootNodes 
            else:
                if(root.val == subRoot.val):
                    subRootNodes.append(root)
                checkLeft =  findSubRootNodes(root.left)
                if(checkLeft):
                    subRootNodes += checkLeft
                checkRight = findSubRootNodes(root.right)
                if(checkRight):
                    subRootNodes += checkRight   
                return  subRootNodes                
 
        def checksubTree(root,subRoot):
            if(root == None and subRoot == None):
                return True
            else:
                if(root == None or subRoot == None or root.val != subRoot.val):
                    return False
                else:
                    return checksubTree(root.left,subRoot.left) and checksubTree(root.right,subRoot.right)
               
 
 
        #Main program
        subTreeNodes = findSubRootNodes(root)
        for subTreeNode in subTreeNodes:            
                isSubtree = checksubTree(subTreeNode,subRoot)
                if(isSubtree):
                    return True
        return False