# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:  

        #The main logic behind this is that if both inorder and preorder are same like inorder and preorder of other tree, then they are identical. But  the node in a tree  are labelled but they may conatin same value so this logic wont work.E.g. p = {2,2,2,null,null,2}, q = {2,2,null,null,2,2}
             
        # def calculatePreInOrder(root):
        #     if(not root):
        #         return []
        #     else:
        #         inorder = []
        #         preorder = []
        #         left = calculatePreInOrder(root.left)
        #         inorder.append(left)
        #         inorder.append(root.val)
        #         right = calculatePreInOrder(root.right)
        #         inorder.append(right)
        #         return inorder

        def sameBinartTrees(p,q):
            if(p==None and q == None):
                return True
            elif(p==None):
                return False
            elif(q==None):
                return False
            else:
                if(p.val!= q.val):
                    return False
                else:
                    isLeftSame = sameBinartTrees(p.left,q.left)
                    isRightSame = sameBinartTrees(p.right,q.right)
                    return (isLeftSame and isRightSame)

            return True


        if(p==None and q == None):
            return True
        else:
            return sameBinartTrees(p,q)



    