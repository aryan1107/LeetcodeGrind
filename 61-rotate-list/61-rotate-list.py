# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_val = []
        curr = head
        while curr:
            list_val.append(curr.val)
            curr = curr.next
        length = len(list_val)
        n_ = [0 for z in range(length)]
        
        for i in range(length):
            n_[(i+k)%length] = list_val[i]
        dummy = ListNode(0)
        curr = dummy
        for i in range(length):
            curr.next = ListNode(n_[i])
            curr = curr.next
        return dummy.next
            