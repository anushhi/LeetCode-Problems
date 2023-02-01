# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self,head):
        count = 0
        while head:
            count+= 1
            head = head.next
        return count
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         #brute force TC -> O(no of nodes*k) SC -> O(1)
#         if head is None or head.next == None:
#             return head
        
#         for i in range(k):
#             temp = head
#             while temp.next.next:
#                 temp = temp.next
#             end = temp.next
#             temp.next = None
#             end.next = head
#             head = end
#         return head
    
        #optimised approach
        if not head or not head.next or k == 0:
            return head
        
        newHead = head
        length = self.length(head)
        while newHead.next:
            newHead =  newHead.next
        newHead.next = head
        if k < length:
            l = length-k
        else:
            k = k%length
            l = length-k
        while l != 0:
            newHead = newHead.next
            l -= 1
        head = newHead.next 
        newHead.next = None
        return head
            
            
        
        
        