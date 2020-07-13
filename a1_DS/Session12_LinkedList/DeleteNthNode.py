'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.


Follow up:

Could you do this in one pass? -- comment: this will be possible using runner technique ; where fast runner moves n-1 times
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertNodes(self,node):
        if self.head==None:
            self.head=node
        else:
            currNode=self.head
            while currNode:
                currNode=currNode.next
            currNode.next=node

    def printLinkedList(self):
        if self.head==None:
            print("Empty LinkedList")
        else:
            currNode=self.head
            while currNode:
                print(currNode.val , end="")
                currNode=currNode.next


    # delete nth node from end of linkedlist - using brute force

    def deleteNthNodeFromEnd(self,n):
        # get length of linkedlist
        ct=0
        temp=self.head
        while temp:
            ct+=1
            temp=temp.next

        # nth node from end is equivalent to length_of_linkedlist -n +1
        # to get above position of node
        pos=ct-n+1

        # edgecase: if 1st node is to be deleted
        if pos==1:
            return self.head.next
        # In next loop we go to pos-1 node ; this is prev_node of the node to be deleted (pos)

        # so we set ct=0 ; since we want to start from beginning
        # start with head node; so set temp=head again


        ct=0
        temp=self.head
        while temp:
            ct+=1
            if pos-1==ct:
                temp.next=temp.next.next
            temp=temp.next
        return self.head



    def deleteNothNodeUsing2pointer(self,n):

        # attach dummy to head of linkedlist to get rid of edge cases
        dummy = Node(0)
        dummy.next=self.head

        # to get fast pointer at position previous to nth node, start both slow & fast pointers at head/dummy, and mobe only fast pointer so that it reaches to previous node

        ct=0
        slow=dummy
        fast=dummy

        # to get fast pointer at position previous to nth node, start both slow & fast pointers at head/dummy, and mobe only fast pointer so that it reaches to previous node

        while(ct<=n):
            fast=fast.next
            ct+=1

            # to get slow pointer at position previous to nth node, start moving both slow & fast pointers ahead
            # by 1position until fast reaches end of linkedlist
        while fast:
            slow=slow.next
            fast=fast.next

        # at the end of while loop slow pointer will reach at exact previous node; and fast is out of linkedlist
        # now using only slow pointer , we connect previous node to next od nth node

        slow.next=slow.next.next

        return dummy.next






