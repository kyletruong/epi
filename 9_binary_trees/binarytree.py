# Binary tree (not BST) for use throughout this chapter

from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # Add new nodes in level-order
    def add(self, x):
        if not self.root:
            self.root = Node(x)
            return

        dq = deque()
        dq.append(self.root)
        while dq:
            root = dq.popleft()
            if not root.left:
                root.left = Node(x)
                break
            else:
                dq.append(root.left)
            if not root.right:
                root.right = Node(x)
                break
            else:
                dq.append(root.right)
