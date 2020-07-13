'''

https://leetcode.com/problems/univalued-binary-tree/

A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.



Example 1:
        1
    1           1
1       1             1

Input: [1,1,1,1,1,null,1]
Output: true

Example 2:

        2
    2       2
5       2


Input: [2,2,2,5,2]
Output: false


Note:
The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].

Approach:
1. Create a global variable outside function called: value=None
2. Edge Case, if root/node (when called in recurssion) is None; return True
4. In function. CHeck if global value is None, set it to hold value of 1st visited Node
3. General Case: If root/node.val!=value ; return False [need to exit as soon as 1st false is hit]
4. Final return to get true both -- recurssions on left & right of Tree should be true
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class univalue:
    value=None

    def uniValue(self,root: Node):
        if not root:
            return True
        if self.value==None:
            self.value=root.val

        if root.val!=self.value:
            return False

        return self.uniValue(root.left) and self.uniValue(root.right)
def main():
    m=univalue()
    rootX = Node(4)
    rootX.left = Node(2)
    rootX.left.left = Node(1)
    rootX.left.right = Node(3)
    rootX.right = Node(8)
    rootX.right.left = Node(6)
    rootX.right.left.left = Node(5)
    rootX.right.left.right = Node(7)
    rootX.right.right = Node(9)
    rootX.right.right.right = Node(10)

    root = Node(4)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right = Node(8)
    root.right.left = Node(6)
    root.right.left.left = Node(5)
    root.right.left.right = Node(7)
    root.right.right = Node(9)


    rootY = Node(4)
    rootY.left = Node(4)
    rootY.left.left = Node(4)
    rootY.left.right = Node(4)
    rootY.right = Node(4)
    rootY.right.left = Node(4)
    rootY.right.left.left = Node(4)
    rootY.right.left.right = Node(4)
    rootY.right.right = Node(4)
    rootY.right.right.right = Node(4)

    print(m.uniValue(root))
    print(m.uniValue(rootY))

if __name__=='__main__':
    main()
