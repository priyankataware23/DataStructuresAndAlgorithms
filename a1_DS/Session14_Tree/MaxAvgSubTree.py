class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class max_avg_subtree:
    max_avg_tree=TreeNode(None)
    max_avg=float('inf')


    def getMaxavgSubtree(self,root:TreeNode):
        if not root:
            return None
        #if not root.left and not root.right:
         #   return None
        self.maxavgTreeHelper(root)
        return self.max_avg_tree



    def maxavgTreeHelper(self,root:TreeNode):
        if not root:
            return (0,0)
        values_left,size_left=self.maxavgTreeHelper(root.left)
        values_right,size_right=self.maxavgTreeHelper(root.right)
        res=(root.val,1)
        values= root.val + values_left + values_right
        size=1+size_left + size_right
        if self.max_avg < (values/size) and root.left and root.right:
            self.max_avg,self.max_avg_tree = (values/size , root)
        return (values,size)

def main():
    mavg=max_avg_subtree()

    root=TreeNode(6)

    root.left=TreeNode(2)
    root.left.left= TreeNode(4)
    root.left.right=TreeNode(1)

    root.right=TreeNode(11)
    root.right.left=TreeNode(-3)
    root.right.right=TreeNode(-2)
    root.right.left.left=TreeNode(3)
    root.right.left.right=TreeNode(1)

    res= mavg.getMaxavgSubtree(root)
    print(res.val)

if __name__=='__main__':
    main()





