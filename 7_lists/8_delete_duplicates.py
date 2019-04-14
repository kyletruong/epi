# Delete duplicates from a sorted linked list of integers

from listnode import ListNode

def delete_duplicates(L):
    itr = L
    while itr is not None:
        next_distinct = itr.next
        while next_distinct is not None and next_distinct.data == itr.data:
            next_distinct = next_distinct.next

        itr.next = next_distinct
        itr = next_distinct
    
    return L

if __name__ == '__main__':
    # 2 -> 2 -> 3 -> 5 -> 7 -> 11 -> 11
    L = ListNode(2)
    L.next = ListNode(2)
    L.next.next = ListNode(3)
    L.next.next.next = ListNode(5)
    L.next.next.next.next = ListNode(7)
    L.next.next.next.next.next = ListNode(11)
    L.next.next.next.next.next.next = ListNode(11)

    L2  = ListNode(2)
    L2.next = ListNode(2)
    L2.next.next = ListNode(2)

    newlist = delete_duplicates(L)
    while newlist is not None:
        print(newlist.data)
        newlist = newlist.next
