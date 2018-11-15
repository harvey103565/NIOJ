# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def array_2_list(raw: list):
    n = len(raw)
    node = None
    if n == 0:
        return node

    node = ListNode(raw[0])
    head = node
    for i in range(1, len(raw)):
        new = ListNode(raw[i])
        node.next = new
        node = new

    return head

def print_list(case):
    s = ''
    while case:
        s += str(case.val) + ' -> '
        case = case.next
    else:
        s += 'None'
    
    print(s)

