# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = ListNode(0)
        evens = ListNode(0)
        oddHead = odds
        evenHead = evens
        isOdd = True
        while head:
            if isOdd:
                odds.next = head
                odds = odds.next 
            else:
                evens.next = head
                evens = evens.next
                
            isOdd = not isOdd
            head = head.next
        evens.next = None
        odds.next = evenHead.next
        return oddHead.next
        