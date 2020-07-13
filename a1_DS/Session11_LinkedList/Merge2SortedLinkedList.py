'''

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

https://leetcode.com/problems/merge-two-sorted-lists/
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertElements(self,node):
        if self.head==None:
            self.head=node
        else:
            lastNode=self.head
            while lastNode:
                lastNode=lastNode.next
            lastNode.next=node

    def printLinkedList(self):
        if self.head==None:
            print("Empty LinkedList")
        else:
            lastNode=self.head
            while lastNode:
                print(lastNode.data, end=" ")

    def merge2sortedLinkedList(self, l1 , l2):
        dummy=Node('a')
        self.head=dummy
        lastNode=self.head
        while l1 and l2:
            if l1.data<=l2.data:
                lastNode.next=l1
                lastNode=l1
                l1=l1.next
            else:
                lastNode.next=l2
                lastNode=l2
                l2=l2.next

        if not l1:
            lastNode.next=l2
            while l2:
                l2=l2.next
        else:
            lastNode.next=l1
            while l1:
                l1=l1.next

        return dummy.next
