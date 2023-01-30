# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,curr):
        nex = None
        prev = None
        
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = fast = slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        slow.next = self.reverse(slow.next)
        slow = slow.next
        
        while slow:
            if slow.val != dummy.val:
                return False
            slow = slow.next
            dummy = dummy.next
        return True
    
            
         
            
            