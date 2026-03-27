def loop_size(node):
    slow, fast = node, node

    while True:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    meeting_point = slow
    count = 1
    current = meeting_point.next
    while current is not meeting_point:
        current = current.next
        count += 1

    return count