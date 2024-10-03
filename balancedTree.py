# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
    #Program for calculating height
        def Height(root):
            if(not root):
                return 0
            elif(not root.left and not root.right): #This condition checks  leaf node
                return 1
            else:
                if(not root.left): #This condition checks that left is nulll 
                    return 1 + Height(root.right)
                elif(not root.right):
                    return 1 + Height(root.left)#This condition checks that left is nulll 
                else:
                    return 1 + max(Height(root.right),Height(root.left))

        def treeBalanced(root):
            if(not root):
                return
            else:
                if(root.left):
                    isLeftTreeBalanced = treeBalanced(root.left)
                    if(not isLeftTreeBalanced):
                        return False
                if(root.right):
                    isRightTreeBalanced = treeBalanced(root.right)  
                    if(not isRightTreeBalanced):
                        return False               
                balancing_factor  = Height(root.left) - Height(root.right) 
                if(not balancing_factor in  range(-1,2)):
                    return False                
            return True

    #Main Program
        if (not root):
            return True
        else:
            return treeBalanced(root)
        
        
#Time Complexity of Above Program is O(n2) 
            