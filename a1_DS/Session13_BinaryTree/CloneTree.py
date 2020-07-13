'''
How to clone a binary tree?
'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class cloneTree:

    def createcloneTree(self,root:TreeNode):
        if not root:
            return None
        copy=TreeNode(root.val)
        copy.left=self.createcloneTree(root.left)
        copy.right=self.createcloneTree(root.right)
        return copy

    def printTree(self,node):
        if not node:
            return
        print(node.val,end =" ")
        self.printTree(node.left)
        self.printTree(node.right)

def main():
    ct=cloneTree()
    root=TreeNode(10)
    root.left=TreeNode(5)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(3)
    root.right =TreeNode(2)
    root.right.left =TreeNode(1)
    root.right.right=TreeNode(6)
    print(ct.printTree(ct.createcloneTree(root)))

if __name__=='__main__':
    main()



