'''
https://leetcode.com/problems/reorder-list/

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or head.next == None:
            return
        # this can be done in  3 steps
        # 1. Split LinkedList into 2 halves. Point end of 1st linkedList to None ; and Mid of given linkedlist will be head of 2nd linkedList
        a, b = self.splitLinkedList(head)

        # 2. Reverse 2nd LinkedList
        b = self.reverseLinkedList(b)

        # 3. Merge 2 linkedlist ; such that alternate elements from 1st linkedlist & reversed LinkedList are appended
        self.merge(a, b)

    def splitLinkedList(self, head: ListNode) -> None:

        slow, fast = head, head
        # using below technique we getmid of linkedlist on the right side
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        nxt = slow.next
        slow.next = None

        return head, nxt

    def reverseLinkedList(self, head: ListNode) -> None:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev

    def merge(self, a, b) -> None:
        while (a and b):
            a.next, a = b, a.next
            b.next, b = a, b.next



