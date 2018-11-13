# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from sys import maxsize

from heapq import heappush, heappop, heapify

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        cursor = head
        n = len(lists)

        while any(lists):
            minimum = maxsize
            mini_i = -1
            for i, l in enumerate(lists):
                if not l:
                    continue

                if l.val <= minimum:
                    minimum = l.val
                    mini_i = i

            cursor.next = lists[mini_i]
            cursor = cursor.next

            lists[mini_i] = lists[mini_i].next

        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = list()

        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))

        head = ListNode(0)
        cursor = head

        while heap:
            v, i, node = heappop(heap)

            if node.next:
                heappush(heap, (node.next.val, i, node.next))

            cursor.next = node
            cursor = cursor.next

        return head.next

            
