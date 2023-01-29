# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self,head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        length = self.length(head)
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while length >= k:
            curr = prev.next
            nex = curr.next
            for i in range(1,k):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr
            length -= k
        return dummy.next
                
                
            
        