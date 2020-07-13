'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?


'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def inOrderHelper(self,node):
        if node.left:
            self.inOrderHelper(node.left)
        self.ans.append(node.val)
        if node.right:
            self.inOrderHelper(node.right)

    def inOrderTraversal(self,root):
        if not root:
            return []
        self.ans=[]
        self.inOrderHelper(root)

        return self.ans
