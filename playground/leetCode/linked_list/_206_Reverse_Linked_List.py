"""
   Given the head of a singly linked list, reverse the list, and return the reversed list.
   Example 1:

   Input: head = [1,2,3,4,5]
   Output: [5,4,3,2,1]
   Constraints:

   The number of nodes in the list is the range [0, 5000].
   -5000 <= Node.val <= 5000

   Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # T O(n), M O(1)
    prev, current = None, head

    while current:
        nxt = current.nxt

        current.nxt = prev
        prev = current

        current = nxt

    return prev


def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
    # Recursive solution :  T O(n), M O(n)
    if not head:
        return None

    newHead = head
    if head.nxt:
        newHead = reverseList2(head.nxt)
        head.nxt.nxt = head
    head.nxt = None

    return newHead


if __name__ == '__main__':
    print("hello world")
