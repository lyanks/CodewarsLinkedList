class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def remove_duplicates(head: Node):
    curnode = head
    while curnode is not None and curnode.next is not None:
        if curnode.data == curnode.next.data:
            curnode.next = curnode.next.next
        else:
            curnode = curnode.next
    return head
