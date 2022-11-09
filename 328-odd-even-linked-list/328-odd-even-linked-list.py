# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(0)
        even = ListNode(0)
        oddHead = odd
        evenHead = even
        isOdd = True
        while head:
            if isOdd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            isOdd = not isOdd
            head = head.next
        even.next = None
        odd.next = evenHead.next
        return oddHead.next