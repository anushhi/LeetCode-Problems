# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #optimised TC -{O(n)} SC - {O(1)}
        # fast = slow = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         return True
        # return False
    
    #BruteForce TC - {O(n)} SC- {O(n)}
        hashmap = {}
        while head:
            if head in hashmap:
                return True
            hashmap[head] = hashmap.get(head,0)+1
            head = head.next
        return False
        