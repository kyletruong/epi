# Merge two sorted lists, resulting list must also be sorted

from listnode import ListNode

def merge_two_sorted_lists(l1, l2):
    # Placeholder for result
    dummyHead = cur = ListNode(-1)

    while l1 and l2:
        if l1.data < l2.data:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    
    # Append remaining nodes
    cur.next = l1 or l2
    return dummyHead.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(5)
    l1.next.next = ListNode(7)

    l2 = ListNode(3)
    l2.next = ListNode(11)

    l3 = merge_two_sorted_lists(l1, l2)

    while l3:
        print(l3.data)
        l3 = l3.next