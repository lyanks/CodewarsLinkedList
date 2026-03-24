def stringify(node):
    if node is None or node.data is None:
        return 'None'
    values = [str(node.data)]
    while node.next is not None:
        values.append(str(node.next.data))
        node = node.next
    values.append("None")
    return ' -> '.join(values)
