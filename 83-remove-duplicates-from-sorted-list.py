# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # a pointer "current" to the head of the linked list
        current = head
        while current is not None and current.next is not None:            
            if current.val == current.next.val:
                # skip one if they are the same
                current.next = current.next.next
            else:
                # move to the next
                current = current.next
        return head
