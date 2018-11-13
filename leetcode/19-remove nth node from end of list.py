# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tail, prev = head, head
        i = 0
        while tail:
            if i > n:
                prev = prev.next
                
            i += 1
            tail = tail.next
            
        if i > n:
            prev.next = prev.next.next

        if i == n:
            return prev.next
            
        return head

    