# Given two non-cyclical lists, find their intersection
# Return the node at the intersection or None if no intersection

from listnode import ListNode

def length(L):
    count = 0
    while L is not None:
        count += 1
        L = L.next

    return count

def listIntersection(L1, L2):
    # Just a quick check to see if we actually have lists
    if L1 is None or L2 is None:
        return None
    
    count1, count2 = length(L1), length(L2)
    diff = abs(count1 - count2)
    if count1 > count2:
        for _ in range(diff):
            L1 = L1.next
    elif count2 > count1:
        for _ in range(diff):
            L2 = L2.next

    while L1 is not None or L2 is not None:
        if L1 is L2:
            break
        L1, L2 = L1.next, L2.next

    return L1

if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)

    head2 = ListNode(-1)
    head2.next = ListNode(0)
    head2.next.next = head1.next

    print(listIntersection(head1, head2).data)
