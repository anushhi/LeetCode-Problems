# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         p1,p2 = list1,list2
        
#         res = p1
#         if list1 == None:
#             return list2
#         if list2 == None:
#             return list1
#         if p1.val > p2.val:
#             p1, p2 = p2, p1
#         while p1 and p2: 
#             temp = None
#             while p1 and p1.val <= p2.val:
#                 temp = p1
#                 p1 = p1.next
#             temp.next = p2
#             p1,p2 = p2,p1
#         return res

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        res = l1
        while l1 and l2:
            temp = None
            while l1 and l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            temp.next = l2
            l1, l2 = l2, l1
        return res

    
    