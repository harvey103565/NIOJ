class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def quick_sort(arr, start, end):
        unsort_sections = list([(start, end)])

        while len(unsort_sections):
            ii, ji = unsort_sections.pop(0)
            i, j = ii, ji
            k = i
            while i != j:
                if k != j:
                    if arr[k] > arr[j]:
                        arr[k], arr[j] = arr[j], arr[k]
                        k = j
                        i += 1
                    else:
                        j -= 1

                if k != i:
                    if arr[i] > arr[k]:
                        arr[i], arr[k] = arr[k], arr[i]
                        k = i
                        j -= 1
                    else:
                        i += 1
            else:
                if i - ii > 1:
                    unsort_sections.append((ii, i - 1))

                if ji - j > 1:
                    unsort_sections.append((j + 1, ji))

        return arr

    @staticmethod
    def sortList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        val_list = list()
        while head:
            next_node = head.next
            head.next = None
            val_list.append(head)
            head = next_node

        val_list = Solution.quick_sort(val_list, 0, len(val_list) - 1)

        next_node = None
        while val_list:
            head = val_list.pop()
            head.next = next_node
            next_node = head

        return head


# arr = [8, 9, 3, 2, 7, 0, 6, 1, 5, 4]
# arr = [1,-3,4,5,8,5,11,14,15,19]
arr = [4,19,14,5,-3,1,8,5,11,15]

arr = Solution.quick_sort(arr, 0, len(arr) - 1)

print(arr)


# link_head = None
# link_tail = None
# for n in arr:
#     node = ListNode(n)
#     if not link_head:
#         link_head = node
#     else:
#         link_tail.next = node
#     link_tail = node
#
# head = link_head
# while head:
#     print(head.val)
#     head = head.next
#
# head = Solution.sortList(link_head)
# while head:
#     print(head.val)
#     head = head.next
#
