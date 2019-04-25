# Check if a binary tree is symmetric
# Symmetrical if can draw a vertical line through the root
# Nodes and structure must be symmetric

from binarytree import BinaryTree, Node
from collections import deque

def symmetric(root):
    if root is None:
        return True

    def check(L, R):
        if not L and not R:
            return True
        elif L and R:
            if L.data != R.data:
                return False
            return check(L.left, R.right) and check (L.right, R.left)

        # One subtree is empty, therefore not symmetric
        return False

    return check(root.left, root.right)

def sym_iterative(root):
    if not root:
        return True
    
    dq = deque()
    dq.append(root.left)
    dq.append(root.right)
    while dq:
        L = dq.popleft()
        R = dq.popleft()
        if not L and not R:
            continue
        if L and R:
            if L.data != R.data:
                return False
            dq.append(L.left)
            dq.append(R.right)
            dq.append(L.right)
            dq.append(R.left)
        else:
            return False

    return True

if __name__ == '__main__':
    left = Node(6)
    left.right = Node(2)
    left.right.right = Node(3)
    right = Node(6)
    right.left = Node(2)
    right.left.left = Node(3)
    root = Node(314, left, right)
    print(symmetric(root))

    nodes = [1,2,2,4,3,3,4]
    tree = BinaryTree()
    for node in nodes:
        tree.add(node)
    print(sym_iterative(tree.root))
