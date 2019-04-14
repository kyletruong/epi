# Given a singly linked list and an integer k, remove the kth last element
# List has at least k nodes
# 1 means last node, k = len(list) would mean first node

from listnode import ListNode

def removeKthElement(L, k):
    dummyHead = ListNode(-1, L)
    first = second = dummyHead
    for _ in range(k):
        first = first.next

    while first.next is not None:
        first, second = first.next, second.next

    second.next = second.next.next
    return dummyHead.next

if __name__ == '__main__':
    L = ListNode(1)
    L.next = ListNode(2)
    L.next.next = ListNode(3)
    L.next.next.next = ListNode(4)
    newlist = removeKthElement(L, 4)
    print(newlist)
    while newlist  is not None:
        print(newlist.data)
        newlist = newlist.next
