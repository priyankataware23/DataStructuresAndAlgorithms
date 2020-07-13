'''
Find diameter: the length of the longest path leaf to leaf

          1
       /    \
      2      3
     / \    / \
    4   5  6   7
     \
      8

In above sample tree longest path leaf to leaf ; including the node that it passes through will be  8 --> 4 --> 2 --> 1 --> 3 --> 7
so formula would be
diameter= max (diameter, length.left + length.right +1) [ +1 to include node that this path passes through]
and at each iteration, we need to find max left on left , right of the tree -- hence we need at each iteration result= 1 + max(left,right) #[Basic formula to get depth/height of the tree]

# below appraoch is using a global variable [diameter]

'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Longest_Path_Leaf_To_Leaf:
    daimeter=0
    def findDiameter_IncludingRootNode(self, root: TreeNode) -> int:
        self.findDepth(root)
        return self.daimeter

    def findDepth(self,root:TreeNode)->int:
        if not root:
            return 0
        left=self.findDepth(root.left)
        right=self.findDepth(root.right)
        self.diameter=max(self.daimeter,1+left+right)
        result=1+ max(left,right)
        return result
def main():
    '''
           1
         /  \
        2    3
       / \
      4   5

    '''
    lp=Longest_Path_Leaf_To_Leaf()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    root.right=TreeNode(3)

    print(lp.findDiameter_IncludingRootNode(root))


if __name__=='__main__':
    main()
