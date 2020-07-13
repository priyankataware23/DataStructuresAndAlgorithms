'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


this is example of bottom's up DFS


'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def minDepth(self,root):
        #base condition
        if not root:
            return 0

        left=self.minDepth(root.left)
        right=self.minDepth(root.right)

        result=1+ min(left,right)

        return result