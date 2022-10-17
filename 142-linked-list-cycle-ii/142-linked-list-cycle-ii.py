# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def detect(head):
            slow,fast = head, head

            while fast != None and fast.next != None:
                
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    return fast
            return None
        
        if head is None:
            return head
        intersect = detect(head)
        if intersect is None:
            return None
        pt1,pt2 = head, intersect
        
        while pt1 != pt2:
            pt1 = pt1.next
            pt2 = pt2.next
        return pt2
        
        

        
        