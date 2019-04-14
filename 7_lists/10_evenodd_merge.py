# Consider a linked list starting at 0 and incrementing by 1
# Split/merge the linked list so first half is even and second half is odd

from listnode import ListNode

def merge(L):
    evenhead, oddhead = ListNode(-1), ListNode(-1)
    evenitr, odditr = evenhead, oddhead
    even_turn = True

    while L:
        if even_turn:
            evenitr.next = L
            evenitr = evenitr.next
        else:
            odditr.next = L
            odditr = odditr.next

        # Alternate betweent True and False
        even_turn ^= True
        L = L.next

    odditr.next = None
    evenitr.next = oddhead.next
    return evenhead.next

if __name__ == '__main__':
    L = ListNode(0)
    L.next = ListNode(1)
    L.next.next = ListNode(2)
    L.next.next.next = ListNode(3)
    L.next.next.next.next = ListNode(4)
    L.next.next.next.next.next = ListNode(5)

    newlist = merge(L)
    while newlist:
        print(newlist.data)
        newlist = newlist.next
