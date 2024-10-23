

"""

use list.next to pass value to the linked list
use list1 = list1.next to move to the next node
https://www.youtube.com/watch?v=E5XXiY6QnAs
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        # current is the pointer
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2

        # avoid the first value 0
        return head.next