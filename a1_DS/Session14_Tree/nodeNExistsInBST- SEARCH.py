'''

Function:SearchInBST is inclass problem; where we return True or false based on if node exists in Tree. Node could exist in left or right side of the tree

Leetcode problem below; should return bst if n is found in BST. -- Since its BST, if root.val>val : val can exists on left side ; else val should be on right side
https://leetcode.com/problems/search-in-a-binary-search-tree/submissions/


'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class SearchInBST:
    def searchNNode(self,root:TreeNode,n:TreeNode)->bool:
        if not root:
             return False
        if root.val==n.val:
            return True
        left=self.searchNNode(root.left,n)
        right=self.searchNNode(root.right,n)
        return left or right # node could be on left or right of tree ; hence or

    def searchBST(self,root:TreeNode,n : int):
        if not root:
            return None
        if root.val==n:
            return root
        elif root.val>n:
            return self.searchBST(root.left,n)
        else:
            return self.searchBST(root.right,n)


def main():
    srch=SearchInBST()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(5)
    root.right.left.right = TreeNode(7)
    root.right.right = TreeNode(9)
    print(srch.searchNNode(root,TreeNode(11)))
    print("==========================")
    print(srch.searchBST(root, 2))
if __name__=='__main__':
    main()
