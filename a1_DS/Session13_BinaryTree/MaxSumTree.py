'''
Sum of all values in Binary Tree

Using bottoms up DFS

'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class sumTree:

    def sumofTree(self,root:TreeNode):
        if not root:
            return 0
        left=self.sumofTree(root.left)
        right=self.sumofTree(root.right)
        result=root.val+left+right
        return result

def main():
    root=TreeNode(5)
    root.left=TreeNode(4)
    root.left.left=TreeNode(9)
    root.left.right=TreeNode(10)
    root.right=TreeNode(12)
    root.right.left=TreeNode(15)
    root.right.right=TreeNode(5)
    s=sumTree()
    print(s.sumofTree(root))
    print("===")
if __name__=='__main__':
    main()
