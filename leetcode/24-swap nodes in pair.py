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
        counter = 0
        new_head, cursor = head, head
        tail, prev = None, head

        while cursor:
            counter += 1

            if counter == 2:
                new_head = cursor

            if counter % 2 == 0:
                if tail:
                    tail.next = cursor
                tail = prev
                cursor.next, cursor = prev, cursor.next
                prev = None
            else:
                prev, cursor = cursor, cursor.next
        else:
            if tail:
                tail.next = prev
        
        return new_head

    def swapPairs_opt(self, head):
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



from helper import array_2_list
from helper import print_list

s = Solution()

raw = [1, 2, 3, 4, 5]
case = array_2_list(raw)

r = s.swapPairs(case)
print_list(r)


raw = [1, 2, 3, 4]
case = array_2_list(raw)

r = s.swapPairs(case)
print_list(r)
