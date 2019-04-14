# Given the head of a singly linked list, find if there's a cycle
# If there's a cycle, return node at start of cycle
# If no cycle, return false

from listnode import ListNode

def cycleLength(head):
    itr, count = head.next, 1
    while itr is not head:
        itr = itr.next
        count += 1
    return count

def hasCycle(head):
    '''
    Using a fast and slow pointer traverse until they are the same
    When you're in the cycle, find the length of the cycle
    Set both fast and slow back to head
    Traverse fast length number of times
    Then traverse both fast and slow by 1 and they will meet at head

    Logic behind this is that if cycle is n length
    If fast pointer is ahead by n length, it will loop back to beginning of
    cycle same time slow pointer reaches beginning
    '''

    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
        if fast is slow:
            length = cycleLength(fast)
            fast = slow = head

            for _ in range(length):
                fast = fast.next
            
            while fast is not slow:
                fast, slow = fast.next, slow.next
            
            return slow
    return None

if __name__ == "__main__":
    # Cyclical part
    head = ListNode(77)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head

    # Non-cylical part
    otherhead = ListNode(-1)
    otherhead.next = ListNode(-2)
    otherhead.next.next = ListNode(-3)
    otherhead.next.next.next = head

    print(hasCycle(otherhead).data)
