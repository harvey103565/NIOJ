# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists_opt(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curosr = head

        while l1 and l2:
            if l1.val < l2.va1:
                curosr.next = l1
                l1 = l1.next
            else:
                curosr.next = l2
                l2 = l2.next
            curosr = curosr.next

        curosr.next = l1 or l2
        return head.next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                if p1.next and p1.next.val < p2.val:
                    p1 = p1.next
                else:
                    p1.next, p1 = p2, p1.next
            else:
                if p2.next and p2.next.val <= p1.val:
                    p2 = p2.next
                else:
                    p2.next, p2 = p1, p2.next

        if l1 and (not l2 or l1.val < l2.val):
            return l1
        else:
            return l2
