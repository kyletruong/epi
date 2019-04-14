from listnode import ListNode

# Given a node in the list, delete that node
# Assume the given node is not the last node in the list

def deleteNode(node):
    node.data = node.next.data
    node.next = node.next.next
