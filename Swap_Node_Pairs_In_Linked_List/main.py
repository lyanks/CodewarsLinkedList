from preloaded import Node


def swap_pairs(head):
    if head is not None and head.next is not None:
        tail = swap_pairs(head.next.next)
        result = head.next
        head.next = tail
        result.next = head
        return result
    return head

    # curnode = head
    # if curnode is not None and curnode.next is not None:
    #     tail = swap_pairs(curnode.next.next)
    #     nextnode = curnode.next
    #     curnode.next = tail
    #     nextnode.next =  curnode
    # return head
