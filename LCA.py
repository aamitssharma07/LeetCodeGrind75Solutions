# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #this function will give the 
        def nodePathRoot(root,input_node):
            if(root.val==input_node.val):
                return [root.val]
            else:
                if(input_node.val>root.val):
                    path = nodePathRoot(root.right,input_node)
                    path.append(root.val)
                    return path
                else:
                    path = nodePathRoot(root.left,input_node)
                    path.append(root.val)
                    return path

        p_path = nodePathRoot(root,p)#Give list with the path nodes of p
        q_path = nodePathRoot(root,q)#Give list with the path nodes of q
        print(p_path)
        print(q_path)
#This loop will give the value of the common ancestor
        index_p = len(p_path)-1
        index_q = len(q_path)-1
        for i in range(len(p_path)):
            if(p_path[index_p]==q_path[index_q]):
                index_p -=1
                index_q -=1
            else:
                break
        

#Based on the valyue search the node na dreturn it
        def nodeSearch(root,p_common):
            if(root.val== p_common):
                return root
            elif(root.val > p_common):
                return nodeSearch(root.left,p_common)
            else:
                return nodeSearch(root.right,p_common)
        return nodeSearch(root,p_path[index_p+1])








       