'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5


https://leetcode.com/problems/partition-list/


'''

'''
# check with instructor
        dummy = ListNode("xyz")
        dummy.next=head
    
        prev=head
        curr=head.next
        
        while curr and curr.next:
            if prev.val>=x and curr.val<x:
                temp=curr.next
                curr.next=dummy.next
                dummy.next=prev.next
                prev.next=temp
            else:
                prev=prev.next
            if dummy.next.val<x:
                dummy=dummy.next
        
        return dummy.next
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def partitionLinkedList(head,x):
    if not head:
        return None

    # Reason to create 2 Linked lists, is to maintain order of elements in Linked list
    # l1 list holds all elements smaller than x, pointer p1 to move ahead as next elements are added
    l1=Node(0)
    p1=l1

    # l2 list holds all elements greater than equal to x , pointer p2 to move ahead as next elements are added
    l2 = Node(0)
    p2=l2

    # pointer p to traverse through linked list
    p=head

    while p:
        # add smaller elements to list1 and move pointer ahead
        if p.val<x:
            p1.next=p
            p1=p1.next
        else:
            # add greater than equal to elements to list2 and move pointer ahead
            p2.next=p
            p2=p2.next
        p=p.next
    # after all elements are added to list's, last pointer should point to None
    # connect last pointer of p1 to 1st element in list 2
    p2.next=None
    p1.next=l2.next
    # return head of partitioned list
    return l1.next

