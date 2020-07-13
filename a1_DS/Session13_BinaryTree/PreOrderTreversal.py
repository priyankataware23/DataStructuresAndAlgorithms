
'''

why doesn't  this work?

   res=[]
        if not root:
            return res

        print(root.val,end=" ")
        res.append(root.val)
        if root.left:
            self.preorderTraversal(root.left)
        if root.right:
            self.preorderTraversal(root.right)
        return res

getting o/p:

Wrong Answer
Runtime: 24 ms
Your input
[1,null,2,3]

stdout
1 2 3

Output
[1]

Expected
[1,2,3]

'''

'''
 3 types of treversal
    a. pre order
    b. in order
    c. post porder

in all 3 treversals, position of root plays important role. And child nodes always come in order -- > left , right 
As name suggests

pre -- root comes first --> root, left, right
in --> root comes in between --> left, root, right
post --> root comes after --> left, right, root


https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/

Below is recussive solution

Time complexity -- O(n)

'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    
    # write helper funtion, we first print / append root, and check if left exists -- traverse left  and then if right exists traverse right
    def preOrderHelper(self,node):
        self.ans.append(node.val)
        if node.left:
            self.preOrderHelper(node.left)
        if node.right:
            self.preOrderHelper(node.right)


    def printPreOrder(self,node):
        if not node:
            return []
        self.ans = []
        self.preOrderHelper(node)
        return self.ans



