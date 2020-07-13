'''



'''

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class longest_Increasing_Path:
    l_i_path=0

    def find_l_i_path(self,root:TreeNode)->int:
        if not root:
            return 0
        self.find_i_path_helper(root)
        return self.l_i_path

    def find_i_path_helper (self,root:TreeNode):
        if not root:
            return 0
        # recur on left side of the tree
        left=self.find_i_path_helper(root.left)

        # recur on right side of the tree
        right=self.find_i_path_helper(root.right)

        # below is used to get longest path length on left side of the tree
        # in If condition, we check if root is smaller than root.left child 
        left_len= 1+ left if root.left and root.val<root.left.val else 1
        right_len= 1+ right if root.right and root.val<root.right.val else 1

        curr_len=max(left_len,right_len)
        self.l_i_path = max (curr_len,self.l_i_path)

        return curr_len

