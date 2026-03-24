from preloaded import Node


def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr is None or list_repr == 'None':
        return None
    values = list_repr.split(' -> ')[:-1]
    head = Node(int(values[0]))
    cur = head
    for el in values[1:]:
        cur.next = Node(int(el))
        cur = cur.next
    return head
