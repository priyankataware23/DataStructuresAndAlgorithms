'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?


'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def postOrderTraversal(self,root):
        if not root:
            return []
        self.res=[]
        self.postOrderTraversalHelper(root)

        return self.res

    def postOrderTraversalHelper(self,node):
        if node.left:
            self.postOrderTraversalHelper(node.left)
        if node.right:
            self.postOrderTraversalHelper(node.right)
        self.res.append(node.val)

