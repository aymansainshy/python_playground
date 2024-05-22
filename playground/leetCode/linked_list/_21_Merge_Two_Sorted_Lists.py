"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_node = ListNode()
    new_head = dummy_node  # head and tail they are pointing to the same ListNode() in memory
    tail = dummy_node

    head1 = list1
    head2 = list2

    while head1 and head2:
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    return new_head.next


if __name__ == '__main__':

    four = ListNode(4)
    two = ListNode(2, four)
    one = ListNode(1, two)

    list1 = one

    # ___________________________________

    four = ListNode(4)
    three = ListNode(3, four)
    one = ListNode(1, three)

    list2 = one

    new_list = mergeTwoLists(list1, list2)

    while new_list:
        print(f"{new_list.val} ->")
        new_list = new_list.next
