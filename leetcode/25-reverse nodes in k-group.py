
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        counter = 0
        new_head = head
        tail, cursor = None, head

        queue = [None] * (k)
        
        while cursor:
            counter += 1
            r = counter % k

            if counter == k:
                new_head = cursor

            queue[r - 1] = cursor
            cursor = cursor.next

            if r == 0:
                for i in range(1, k):
                    queue[k - i].next = queue[k - i - 1]
                else:
                    if tail:
                        tail.next = queue[k - 1]
                    tail = queue[0]
            queue[r] = None

        else:
            if tail:
                tail.next = queue[0]
        
        return new_head


from helper import array_2_list
from helper import print_list

s = Solution()

raw = [1, 2, 3, 4, 5]
case = array_2_list(raw)

r = s.reverseKGroup(case, 3)
print_list(r)
