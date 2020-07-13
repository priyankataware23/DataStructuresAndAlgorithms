'''
https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class symmetricTree:
    def isSymmetric(self,root:TreeNode)->bool:
        # this will need a nested function [ function within function - you can name it as helper function], as we need to compare left side of tree with right side of tree,
        # which means we need to pass 2 nodes at a time, to decide whether pass or fail at each recursion

        def isSymmetricHelper(root1:TreeNode,root2:TreeNode):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val!=root2.val:
                return False
            return isSymmetricHelper(root1.left,root2.right) and isSymmetricHelper(root1.right,root2.left)
        if not root:
            return True
        return isSymmetricHelper(root,root)

def main():
    st=symmetricTree()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.left.left=TreeNode(3)
    root.left.right=TreeNode(4)
    root.right =TreeNode(2)
    root.right.left =TreeNode(4)
    root.right.right=TreeNode(3)
    print(st.isSymmetric(root))
    print("=================")

    rootX=TreeNode(1)
    rootX.left=TreeNode(2)
    rootX.left.right=TreeNode(3)
    rootX.right =TreeNode(2)
    rootX.right.right=TreeNode(3)
    print(st.isSymmetric(rootX))

if __name__=='__main__':
    main()