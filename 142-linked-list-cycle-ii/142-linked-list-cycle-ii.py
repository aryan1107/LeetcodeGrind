# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        curr = head
        if not head:
            return head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                intercept = slow
                if intercept is None:
                    return intercept
                while curr != intercept:
                    curr = curr.next
                    intercept = intercept.next
                return curr
        return None