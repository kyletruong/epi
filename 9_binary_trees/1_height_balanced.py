# Check if binary tree is height-balanced
# Difference in height of left sub-tree and right-subtree is at most 1

from binarytree import BinaryTree, Node
from collections import namedtuple

def is_balanced(root):
    # namedtuple makes it more expensive but more readable
    Node = namedtuple('Node', ['balanced', 'height'])
    def check_tuple(root):
        if root is None:
            return Node(True, -1)

        l = check_tuple(root.left)
        if not l.balanced:
            return Node(False, 0)

        r = check_tuple(root.right)
        if not r.balanced:
            return Node(False, 0)

        # Subtrees are balanced
        balance = abs(l.height - r.height) <= 1
        height = max(l.height, r.height) + 1
        return Node(balance, height)

    # Realize that I can use negative int to indicate false, but less readable
    def check_int(root):
        if not root:
            return 0

        # By checking -1 right after, can avoid looking at every single node
        # So if -1, keep throwing that back up and skip recursive calls
        l = check_int(root.left)
        if l == -1:
            return -1
        r = check_int(root.right)
        if r == -1:
            return -1

        if abs(l - r) > 1:
            return -1
        return max(l, r) + 1

    return check_int(root) != -1

if __name__ == '__main__':
    subroot = Node(2)
    subroot.left = Node(3)
    subroot.left.left = Node(4)
    subroot.left.right = Node(4)
    root = Node(1)
    root.right = Node(2)
    root.left = subroot
    print(is_balanced(root))

    r = Node(2)
    r.left = Node(2)
    r.right = Node(2)
    r.right.right = Node(3)
    r.left.right = Node(4)
    print(is_balanced(r))
