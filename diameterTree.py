
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        tree_diameter = 0
        def diameter_tree(root):
            nonlocal tree_diameter
            node_diameter = 0
            if(not root):
                return 0
            # elif(root.left==None and root.right==None):
            #     return 1
            else:
                left_height = diameter_tree(root.left)
                right_height = diameter_tree(root.right)
                node_diameter = left_height + right_height + 1
                if(tree_diameter<node_diameter):
                     tree_diameter = node_diameter
                return  1+ max(left_height,right_height)
       
 
        #Main Progran
        diameter_tree(root)
        return tree_diameter
    



#Input Tree
root = TreeNode(1)
root.left = TreeNode(2)

print(Solution().diameterOfBinaryTree(root))

