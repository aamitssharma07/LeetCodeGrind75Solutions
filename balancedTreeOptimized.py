#Above program can be optimized in O(n). The main logic of teh belwo progarm is from the leaf node start checking that is there any imbalance. I there is imbalance return False, else retirn the Height of the Node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        def checkBalance(root):
            left_height = 0
            right_height = 0
            if(not root):
                return 0
            elif(root.left==None and root.right==None):
                return 1
            else:
                if(root.left):
                    left_height = checkBalance(root.left)
                    if(left_height==False):
                        return False

                if(root.right):
                    right_height = checkBalance(root.right)
                    if(right_height==False):
                        return False                    
                balance_factor = left_height - right_height
                if(not balance_factor in range(-1,2)):
                    return False
                else:
                    return 1 + max(left_height, right_height)
            return True


        #Main program
        if(not root):
            return True
        else:
            if(checkBalance==False):
                return False
            else:
                return True
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)           
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
print(Solution().isBalanced(root))