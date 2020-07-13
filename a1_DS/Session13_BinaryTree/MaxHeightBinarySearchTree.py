'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def maxDepth(self,root):
        # base condition
        if not root:
            return 0

        # general condition
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)

        # for each iteration result is computed
        result=1+max(left,right)

        return result
