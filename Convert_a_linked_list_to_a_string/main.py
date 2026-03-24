class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    values = []
    while node.next is not None:
        values.append(node.data)
        node = node.next
    values.append(None)
    return ' -> '.join(values)

