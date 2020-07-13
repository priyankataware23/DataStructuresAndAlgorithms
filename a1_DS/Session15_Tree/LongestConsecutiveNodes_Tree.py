'''

Approach:
go bottoms-up dfs technique

1. we create a global variable named: long_cons_path=0 ; which will initially hold 0.
During each recurssion on left side / right side of the tree this variable will be updated.

2. Since we are using a global variable, main comparision of longest-path on left / right of tree & computing of global variable will occur in helper function
3. final longestpath function calls helper function & returns global variable


In helper function

1. this helper function, accepts root & returns longest path that could be either on left or right side -- return type -> int
2. within this function, we recur on left side, and right side using helper function
3. compute left length --- > if root.left.val - root.val ==1 then 1 (include current left iteration) + left (value computed till previous iteration) else 1
    similar on right lenght -->if root.right.val - root.val ==1 then 1 (include current right iteration) + right (value computed till previous iteration) else 1
 4. Pick longest length amongst left & right
 5. update global variable
'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class LongestConsecutivePath:
    lcpath=0

    def findLongestConsecutivePath(self,root:TreeNode)->int:
        if not root:
            return 0
        self.findLongestConsecutivePathHelper(root)
        return self.lcpath

    def findLongestConsecutivePathHelper(self,root:TreeNode):
        if not root:
            return 0

        left=self.findLongestConsecutivePathHelper(root.left)
        right=self.findLongestConsecutivePathHelper(root.right)

        left_len= 1 + left if root.left and (root.left.val - root.val) ==1 else 1
        right_len= 1 + right if root.right and (root.right.val - root.val) ==1 else 1
        curr_len=max(left_len,right_len)

        self.lcpath= max(self.lcpath,curr_len)

        return curr_len
'''
   1
    \
     3
    / \
   2   4
        \
         5
         '''
def main():
    lcp=LongestConsecutivePath()
    root=TreeNode(1)
    root.right=TreeNode(3)
    root.right.left=TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)

    result=lcp.findLongestConsecutivePath(root)
    print(result)

if __name__=='__main__':
    main()



