# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s, p = head, head

        if head:
            s = head.next
            if s:
                s.next, head.next = head, self.swapPairs(s.next)
                return s

        return head
