class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def merge_sort(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        if not head.next.next:
            return Solution.merge_list(head, head.next)

        right_head = head
        left_tail = None
        tail = head
        while tail.next:
            tail = tail.next
            left_tail = right_head
            right_head = right_head.next

            if not tail.next:
                break

            tail = tail.next
        left_tail.next = None

        left = Solution.merge_sort(head)
        right = Solution.merge_sort(right_head)

        return Solution.merge_list(left, right)

    @staticmethod
    def merge_list(left, right):
        if left.val < right.val:
            merged_tail = left
            left = left.next
        else:
            merged_tail = right
            right = right.next
        merged_head = merged_tail
        merged_tail.next = None

        while left and right:
            if left.val < right.val:
                next_node = left
                left = next_node.next
            else:
                next_node = right
                right = next_node.next
            merged_tail.next = next_node
            merged_tail = merged_tail.next
            merged_tail.next = None
        else:
            if left:
                merged_tail.next = left
            else:
                merged_tail.next = right

        return merged_head


# arr = [8, 9, 3, 2, 7, 0, 6, 1, 5, 4]
# arr = [1,-3,4,5,8,5,11,14,15,19]
arr = [4, 19, 14, 5, -3, 1, 8, 5, 11, 15]


link_head = None
link_tail = None
for n in arr:
    node = ListNode(n)
    if not link_head:
        link_head = node
    else:
        link_tail.next = node
    link_tail = node

head = link_head
while head:
    print(head.val)
    head = head.next

head = Solution.merge_sort(link_head)
while head:
    print(head.val)
    head = head.next



