'''

https://leetcode.com/problems/diameter-of-binary-tree/

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class diameterBST:
    diameter=0
    def finddiameter(self,root:TreeNode)->int:
        self.findDepth(root)
        return self.diameter

    def findDepth(self,root:TreeNode)->int:
        if not root:
            return 0
        left= self.findDepth(root.left)
        right=self.findDepth(root.right)
        self.diameter= max(self.diameter,left+right)
        result= 1+ max(left,right)
        return result


def main():
    '''
           1
         /  \
        2    3
       / \
      4   5

    '''
    dia=diameterBST()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    root.right=TreeNode(3)

    print(dia.finddiameter(root))


if __name__=='__main__':
    main()
