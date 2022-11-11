# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head.next #stores the curr element
        #create and initialise a node to track the head of the sorted list
        sorted_head = ListNode(val = -5000 , next = head)
        last_sorted = head
        
        while(curr):
            if last_sorted.val <= curr.val:
                last_sorted = last_sorted.next
            else:
                prev = sorted_head
                while prev.next.val <= curr.val:
                    prev = prev.next
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
        
            curr = last_sorted.next
        return sorted_head.next
    

        

            
            
        
        
        
        
        