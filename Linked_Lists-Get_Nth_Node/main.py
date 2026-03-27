from preloaded import Node


def get_nth(node, index):
    if index < 0:
        raise IndexError
    cur = node
    i = 0
    while i < index:
        if cur.next is None:
            raise IndexError
        cur = cur.next
        i += 1
    if i == index:
        return cur
    raise IndexError