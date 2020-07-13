'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

            3
        /      \
        5       1
       / \     / \
      6   2   0   8
         / \
        7   4



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


-- Approach, using Bottoms up DFS,
1. we will check id node p or q exists in tree, if node exists mark that node as True, and final return of the recursion will be true, if node exists in left or right of the tree
2. We will Create a global variable lca and initial will be set to None
3. During each recurssion this global variable will be set root. If both left and right of root are True. This condition works if the 2 given nodes fall on different path -- i.e. 1 on left and other on right
4. If both nodes fall on same paths then condition will be either root.val ==p.val or root.val==q.val and either left or right node if the root is true then set LCA=root

Complexity - O(n) -- since we visit all nodes


'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class LowestCommonAncestor:
    #use of global variable to hold final answer
    lca=None
    def findLowestCommonAncestor(self,root:TreeNode, p:TreeNode, q:TreeNode)->TreeNode:
        # base condition check
        if not root:
            return None
        self.findLowestCommonAncestorHelper(root,p,q)
        return self.lca
    def findLowestCommonAncestorHelper(self, root:TreeNode,p:TreeNode,q:TreeNode)->bool:
        # base condition
        if not root:
            return False
        # recur on left side of the tree to check if node p or q exists on left side.
        left=self.findLowestCommonAncestorHelper(root.left,p,q)

        # recur on right side of the tree to check if node p or q exists on right side.
        right=self.findLowestCommonAncestorHelper(root.right,p,q)

        # Edge case where root itself is p or q, and one of the node is already found on same path as that of root itself

        if (root.val==p.val or root.val==q.val) and (left or right):
            self.lca=root
        # condition to check of p or q exists; anf if found set that node iteration to true -- this same condition is called for both left & right recurssion
        if root.val==p.val or root.val==q.val:
            return True

        # below condition will be applied only to Lowest common ancestor; as only on ancestor; both right & left of the tree will be true
        if left and right:
            self.lca=root
        # this is the return statement for each recursion, this is mainly to set root to True if either left or right of the root is True [which means -- p or q was found on either side of root]
        return left or right
'''
            3
        /      \
       5        1
       / \     / \
      6   2   0   8
         / \
        7   4
'''
def main():
    l=LowestCommonAncestor()

    root=TreeNode(3)

    root.left=TreeNode(5)
    root.left.left=TreeNode(6)
    root.left.right=TreeNode(2)

    root.left.right.left=TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right=TreeNode(1)
    root.right.left=TreeNode(0)
    root.right.right=TreeNode(8)

    result=l.findLowestCommonAncestor(root,TreeNode(6),TreeNode(0) )
    print(result.val)

    print("=======================================")

    result = l.findLowestCommonAncestor(root, TreeNode(5), TreeNode(1))
    print(result.val)

    print("=======================================")

    result = l.findLowestCommonAncestor(root, TreeNode(5), TreeNode(4))
    print(result.val)

if __name__=='__main__':
    main()







