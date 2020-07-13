'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

https://leetcode.com/problems/remove-linked-list-elements/
'''


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None



    def insertElements(self,data):
        if self.head==None:
            self.head=data

        else:
            lastNode=self.head
            while lastNode.next:
                lastNode=lastNode.next
            lastNode.next=data



    def insert(self,data):
        if self.head==None:
            self.head=data
        else:
            lastNode=self.head # consider head as last item in linkedlist
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next=data


    def printLinkedList(self):
        lastNode=self.head
        if lastNode==None:
            print("Linked List is empty")
        while lastNode:
            print(lastNode.data ,end=" ")
            lastNode=lastNode.next

    def removeElementsFromLinkedList(head,val):
        #handle edge cases with head, make code concise ; In dummy append any value, operate on linkedlist, return dummy.next-- to get rid of dummy
        dummy = Node(0) #create a dummy node with any value
        dummy.next = head  #prepend dummy to head

        # Now dummy head for sure is not a val to delete
        prev_node=dummy
        curr_node=dummy.next

        while curr_node:# basic while keep simple, deal with current_node only, not to many adjacent nodes
            #delete the curr node
            if curr_node.val==val:
                prev_node.next=curr_node.next
                curr_node=curr_node.next
            else:
                prev_node=curr_node
                curr_node=curr_node.next

        return dummy.next #discard dummy node


def main():
    llist=LinkedList()
    l = LinkedList()
    llist.insertElements(Node(1))
    llist.insertElements(Node(2))
    llist.insertElements(Node(6))
    llist.insertElements(Node(3))
    llist.insertElements(Node(4))
    llist.insertElements(Node(6))
    llist.insertElements(Node(6))
    llist.insertElements(Node(14))
    llist.printLinkedList()
    print()
    print("================")
    l.removeElementsFromLinkedList(llist,3)




if __name__=='__main__':
    main()















