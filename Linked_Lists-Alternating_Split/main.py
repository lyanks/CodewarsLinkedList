class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise Exception("List too short")
    odd_last, even_last = head, head.next
    odd, even = odd_last, even_last
    is_odd = True
    curnode = head.next.next
    while curnode is not None:
        queue = curnode
        curnode = curnode.next
        queue.next = None
        if is_odd:
            odd_last.next = queue
            odd_last = queue
        else:
            even_last.next = queue
            even_last = queue
        is_odd = not is_odd
    odd_last.next = None
    even_last.next = None
    return Context(odd, even)
