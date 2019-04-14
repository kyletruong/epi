# Test whether a singly linked list is a palindrome

from listnode import ListNode

def isPalindrome(L):
    # True for empty list and single node
    if L is None or L.next is None:
        return True

    # Slow will end up 1 node before second half that needs to be reversed
    slow = fast = L
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next

    # Reverse second half
    tail = slow.next
    while tail.next:
        temp = tail.next
        tail.next = temp.next
        temp.next = slow.next
        slow.next = temp

    # Now compare first half to second half
    slow = slow.next
    while slow:
        if slow.data != L.data:
            return False
        slow, L = slow.next, L.next

    return True

if __name__ == '__main__':
    L = ListNode('a')
    L.next = ListNode('b')
    L.next.next = ListNode('b')
    L.next.next.next = ListNode('a')
    L.next.next.next.next = ListNode('c')
    A = ListNode('c', L)

    print(isPalindrome(A))
