def loop_size(node):
    if node.next is None or node.next.next is None:
        return None
    slow, fast = node, node
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    else:
        return 0
    count = 1
    current = slow.next
    while current != slow:
        current = current.next
        count += 1
    return count
