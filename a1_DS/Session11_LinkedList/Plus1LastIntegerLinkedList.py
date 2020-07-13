'''
https://leetcode.com/articles/plus-one-linked-list/
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertElemensts(self,node):
        if self.head==None:
            self.head=node
        else:
            lastNode=self.head
            while lastNode:
                lastNode=lastNode.next
            lastNode.next=node

    def printLinkedList1(self):
        currNode = self.head
        if currNode == None:
            print("LinkedList is empty")
            return
        while currNode:
            print(currNode.data, end=" ")
            currNode = currNode.next

    def incrementLastInteger(self,node):
        dummy=Node(0)
        dummy.next=self.head
        lastNotNine=dummy
        while self.head:
            if self.head.val!=9:
                lastNotNine=self.head
            self.head=self.head.next

        lastNotNine.val +=1
        lastNotNine=lastNotNine.next

        while lastNotNine:
            lastNotNine.val=0
            lastNotNine=lastNotNine.next

        return dummy if dummy.val>0 else dummy.next

def main():
    list=LinkedList()
    list.insert(Node(1))
    list.insert(Node(2))
    list.insert(Node(4))
    list.printLinkedList1()

if __name__=='__main()__':
    main()






