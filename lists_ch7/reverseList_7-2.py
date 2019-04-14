# Reverse a list from start to finish
# Start begins at 1 and finish is inclusive

from listnode import ListNode

def reverse_sublist(L, start, finish):
    subhead = dummyhead = ListNode(-1, L)
    for _ in range(1, start):
        subhead = subhead.next

    subtail = subhead.next
    for _ in range(start, finish):
        temp = subtail.next
        subtail.next = temp.next
        temp.next = subhead.next
        subhead.next = temp

    return dummyhead.next

# Reverse an entire list without allocating any additional nodes
def reverse_sublist2(L):
    head = L

    while L.next is not None:
        temp = L.next
        L.next = temp.next
        temp.next = head
        head = temp

    return head

if __name__ == "__main__":
    L = ListNode(1)
    L.next = ListNode(2)
    L.next.next = ListNode(3)
    L.next.next.next = ListNode(4)

    newlist = reverse_sublist2(L)

    while newlist:
        print(newlist.data)
        newlist = newlist.next
