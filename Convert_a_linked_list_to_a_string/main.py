class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    if node.data is None:
        return 'None'
    values = [str(node.data)]
    while node.next is not None:
        values.append(str(node.next.data))
        node = node.next
    values.append("None")
    return ' -> '.join(values)
