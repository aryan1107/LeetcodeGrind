# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            temp_next = slow.next
            slow.next = prev
            prev = slow
            slow = temp_next
        curr = head
        while prev:
            if prev.val != curr.val:
                return False
            curr = curr.next
            prev = prev.next
        return True