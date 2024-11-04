# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if(root.left ==None and root.right ==None):
        return 0
    else:
        lefTreeHeight = 0
        rightTreeHeight = 0
        if(root.left):
            lefTreeHeight = height(root.left)
        if(root.right):   
            rightTreeHeight = height(root.right)
        heightTree = 1 + max(lefTreeHeight,rightTreeHeight)
    return heightTree
    
    
head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(4)
head.right.right = TreeNode(4)
print(height(head))