class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head: Node):
    if head is None:
        return None
    revers = head
    tail = Node(revers.data)
    while revers.next is not None:
        revers = revers.next
        head = Node(revers.data)
        head.next = tail
        tail = head
    return tail
