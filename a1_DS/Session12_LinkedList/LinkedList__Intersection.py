'''
https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/


'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    p1 = headA
    p2 = headB

    while p1 and p2:
        if p1 == p2:
            return p1
        p1 = p1.next
        p2 = p2.next

        if not p1:
            p1 = headB

        if not p2:
            p2 = headA
    return None


def intersectionLinkedList(self, headA:ListNode, headB:ListNode)->ListNode:
    if not headA or not headB:
        return None
# if allocated in pythonic way, execution time reduces
    a,b=headA,headB
    la,lb=0,0
    #Get length of linkedList 1, we use head instead of pointers because we want pointers (a & b) to be derived based on diff & to finally traverse through linkedlist
    while headA:
        la += 1
        headA=headA.next

    # Get length of linkedList 2
    while headB:
        lb += 1
        headB=headB.next


    if (la > lb):
        diff = la - lb
        # identify start position of pointers- a
        while diff:
            a=a.next
            diff-=1
    elif (lb>la):
        diff= lb - la
        # identify start position of pointers- b
        while diff:
            b=b.next
            diff-=1

    while (a and b):
        if a==b:
            return a
        a=a.next
        b=b.next
    return None






