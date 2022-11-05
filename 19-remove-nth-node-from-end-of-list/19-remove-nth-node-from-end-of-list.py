# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #reverse
        curr = head
        prev = None
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        if n == 1:
            prev = prev.next
            new_curr = prev
            new_prev = None
            while new_curr:
                temp_next = new_curr.next
                new_curr.next = new_prev
                new_prev = new_curr
                new_curr = temp_next
            return new_prev
        i = 1
        curr = prev
        while curr.next:
            if i+1 == n:
                curr.next = curr.next.next
            else:
                curr = curr.next
            i+=1
        
        new_curr = prev
        new_prev = None
        while new_curr:
            temp_next = new_curr.next
            new_curr.next = new_prev
            new_prev = new_curr
            new_curr = temp_next
        return new_prev