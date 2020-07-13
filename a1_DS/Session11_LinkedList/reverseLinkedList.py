'''
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


'''

class Node:
    def __init__(self,val):
        self.val=val
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
                print(lastNode.val ,end=" ")
                lastNode=lastNode.next


    #iterative
    def reverseLinkedList(self,node):
        prev=None
        while self.head:
            temp=self.head # hold current head in temp, and this will be used to point to prev, which is to reverse pointers instead of focusing on val for node
            self.head=self.head.next # move head to next node
            temp.next=prev # point current head to prev node; i.e. reverse direction of pointer
            prev=temp # move prev to next node
        return prev # return prev as at end of loop head points to None


