# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # If removing the head
        if fast is None:
            return head.next

        # Move both pointers
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Remove nth node from end
        slow.next = slow.next.next

        return head
           
        