# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Brute Force - TC -{O(m*n),SC -{O(1)}}
        # while(headA):
        #     temp = headB
        #     while temp:
        #         if headA == temp:
        #             return headA
        #         temp = temp.next
        #     headA = headA.next
        # return None
        # Optimised approach TC -{O(m+n) ,SC -{O(n)}}
        listSet = set()
        while headA:
            listSet.add(headA)
            headA = headA.next
        while headB:
            if headB in listSet:
                return headB
            headB = headB.next
        return None
        