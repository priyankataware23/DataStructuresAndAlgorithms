'''
https://leetcode.com/problems/balanced-binary-tree/submissions/
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

below approach is using global variable
'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class balanced_BST:
    #create a global variable which needs to be updated at end of each iteration
    isbalanced=False
    def isBalancedTree(self,root:TreeNode)->bool:
        if not root:
            return True
        self.findDepth(root)
        return self.isbalanced

    def findDepth(self,root:TreeNode)->int:
        if not root:
            return 0
        left=self.findDepth(root.left)
        right=self.findDepth(root.right)
        self.isbalanced = (self.isbalanced and (True if abs(left - right) <=1 else False))
        return 1+ max(left,right)

def main():
    bst=balanced_BST()

    root=TreeNode(1)
    root.left=TreeNode(2)
    root.left.left=TreeNode(3)
    root.left.right=TreeNode(3)
    root.left.left.left=TreeNode(4)
    root.left.left.right = TreeNode(4)
    root.right=TreeNode(2)

    print(bst.isBalancedTree(root))

    rootY=TreeNode(3)
    rootY.left=TreeNode(9)
    rootY.right=TreeNode(20)


    print(bst.isBalancedTree(rootY))




if __name__=='__main__':
    main()
