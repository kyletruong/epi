"""
Given two nodes (no parent field) compute the LCA in a binary tree
"""

from binarytree import BinaryTree

class LCA:
    def __init__(self):
        self.lca_node = None

    # Python classmethods don't require objects similar to static methods
    @classmethod
    def compute(cls, root, p, q):
        if not root:
            return None

        def check(root):
            if not root:
                return 0

            L = check(root.left)
            if L == 2:
                return 2
            R = check(root.right)
            if R == 2:
                return 2

            found = root is p or root is q
            M = 1 if found else 0

            if M + L + R == 2:
                cls.lca_node = root
            return M + L + R

        check(root)
        return cls.lca_node.data


if __name__ == '__main__':
    bt = BinaryTree()
    for i in range(1, 16):
        bt.add(i)
    p = bt.root.left.left.right
    q = bt.root.left.right.right

    print(LCA.compute(bt.root, p, q))
