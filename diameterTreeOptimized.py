# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Variable to store the maximum diameter (longest path between any two nodes in the tree)
        tree_diameter = 0

        # Helper function to calculate the height of the tree and update the diameter
        def diameter_tree(root):
            nonlocal tree_diameter  # Allows modification of the outer variable tree_diameter
            if not root:
                # If the node is None (base case), return height as 0
                return 0  
            elif(root.left ==None and root.right==None):
                return 1
            else:
                left_height = 0

                right_height = 0
                # Recursively compute the height of the left subtree
                if(root.left):
                    left_height = diameter_tree(root.left)  
                # Recursively compute the height of the right subtree
                if(root.right):
                    right_height = diameter_tree(root.right)
                
                # The diameter through this node would be the sum of left and right subtree heights
                node_diameter = left_height + right_height
                
                # Update the global tree_diameter if the current node's diameter is larger
                if tree_diameter < node_diameter:
                    tree_diameter = node_diameter
                
                # Return the height of the current node, which is 1 + maximum of left or right subtree height
                return 1 + max(left_height, right_height)
       
        # Call the helper function to compute diameter starting from the root node
        diameter_tree(root)
        # Return the final diameter value
        return tree_diameter
