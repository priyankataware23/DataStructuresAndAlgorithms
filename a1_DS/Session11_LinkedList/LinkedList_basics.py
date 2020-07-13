class Node:
    # function to initialize Node object, in this initialization, when node call is called with some data point, like: Node("item"), then that item is assigned to Node and next of note is set to None
    def __init__(self,node):
        self.data=node # Assign data
        self.next=None # Assign next as null
class LinkedList:
    # initialize LinkedList class
    def __init__(self):
        self.head=None # when this class is initialized head object is created and is set to None

 # insert method accepts items to be added to LinkedList
    def insert(self,data):
        if self.head==None:
            self.head=data
        else:
            lastNode=self.head # consider head as last item in linkedlist
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next=data

# add new head
    def insertNewHead(self,node):
        if self.head==None:
            self.head=node
        node.next=self.head
        self.head=node

# add Node after given Node
    def insertAfter(self,prev_node,node):
        if prev_node==None:
            return "Invalid Node"
        lastNode=self.head
        print("lastNode before while: ",lastNode.data)
        while lastNode:
            if lastNode.data==prev_node.data:
                print("if: ",lastNode.data)
                node.next=lastNode.next
                lastNode.next=node
            elif lastNode.next==None:
                break
            lastNode=lastNode.next

    def insertBefore(self,given_node,node):
        if given_node==None:
            return "Invalid Node"
        lastNode=self.head
        prevNode=lastNode
        while lastNode:
            if lastNode.data==given_node.data:
                prevNode.next=node
                node.next=lastNode
            elif lastNode.next==None:
                break
            prevNode=lastNode
            lastNode=lastNode.next


    def deleteNode(self,node):
        if node==None:
            return "Invalid Node"
        prevNode=self.head
        currNode=self.head

        if currNode.data==node.data:
            self.head=currNode.next
            del currNode
        while currNode:
            if currNode.data==node.data:
                prevNode.next=currNode.next
            elif currNode.next==None:
                break
            prevNode=currNode
            currNode=currNode.next


    def deleteLastNode(self):
        prev_node=self.head
        curr_node=self.head

        if curr_node.next==None:
            self.head=None

        while curr_node:
            if curr_node.next==None:
                break
            prev_node=curr_node
            curr_node=curr_node.next
        prev_node.next=curr_node.next
        del curr_node



    def findLastNodeWithKeyValue(self,node):
        lastNode=self.head
        ct=1
        k_ct=0
        if lastNode.data==node.data and lastNode.next==None:
            k_ct=ct
            return k_ct
        while lastNode:
            if lastNode.data==node.data:
                k_ct=ct
            lastNode=lastNode.next
            ct+=1
        return k_ct




#convert Array to LinkedList
    def convertArray2LinkedList(self,arr):
        if arr==None:
            return "Invalid Array"
        for i in range(len(arr),0,-1):
            if self.head==None:
                self.head=Node(i)
            else:
                Node(i).next=self.head
                self.head=Node(i)
        return self.head


    def printLinkedList(self):
        currNode=self.head
        if currNode==None:
            print("LinkedList is empty")
            return
        while True:
            if currNode==None:
                break
            print(currNode.data , end=" ")
            currNode=currNode.next

def main():
    llist=LinkedList()
    llist.insert(Node("John"))
    llist.insert(Node("Matt"))
    llist.insert(Node("Nolan"))
    llist.insert(Node("Lincoln"))
    llist.insert(Node("George"))
    print(llist.printLinkedList())

    print("=============")
    llist.insertNewHead(Node("new_head"))
    print(llist.printLinkedList())

    '''
    arr=[1,2,3,4,5,6,7,8,9,10]
    item= llist.convertArray2LinkedList(arr)
    while item.next:
        print(item.data , end=" ")
    '''
    print("=============")
    llist.insertAfter(Node("Nolan"),Node("Eric"))
    print(llist.printLinkedList())
    print("=============")
    llist.insertBefore(Node("Nolan"),Node("Sadaf"))
    llist.printLinkedList()

    print("==============")
    llist.deleteNode(Node("Eric"))
    print(llist.printLinkedList())

    print("=================")
    llist.deleteLastNode()
    print(llist.printLinkedList())

    print("=================")
    llist.insert(Node("Nolan"))
    llist.insert(Node("Nolan"))
    llist.insert(Node("Nolan"))
    llist.insert(Node("Nolan"))
    print(llist.printLinkedList())
    print(llist.findLastNodeWithKeyValue(Node("Nolan")))

if __name__=='__main__':
    main()




