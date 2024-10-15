class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def calculatePreInOrder(root):
    if(not root):
        return [], [], []
    else:
        inorder = []
        preorder = []
        postorder = []
        preorder.append(root.val)
        leftInorder, leftPreorder, leftPostOrder  = calculatePreInOrder(root.left)
        inorder += leftInorder
        preorder += leftPreorder
        postorder += leftPostOrder
        inorder.append(root.val)
        rightInorder, rightPreorder, rightPostorder  = calculatePreInOrder(root.right)
        inorder += rightInorder
        preorder += rightPreorder
        postorder += rightPostorder
        
        postorder.append(root.val)
        return inorder,preorder,postorder


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(calculatePreInOrder(root))


