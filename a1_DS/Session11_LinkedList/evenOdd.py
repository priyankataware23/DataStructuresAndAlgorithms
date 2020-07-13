'''
https://leetcode.com/problems/odd-even-linked-list/submissions/

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL


Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].


'''


def oddEvenList(self, head):
    if head == None:
        return head
    odd = head  # 1st odd position
    even = head.next  # 1st even position
    evenHead = even  # connect last odd with evenHead
    while odd and even and odd.next and even.next:
        odd.next = even.next # attach next odd
        odd = even.next # move odd to next odd
        even.next = odd.next # attach next even
        even = odd.next # move even to next even
    odd.next = evenHead  # connect odd with even
    return head
