# Question from chapter 8
# Given a binary tree, return array consisting of keys at the same level
# Keys at the same level are in a subarray in the master array

from binarytree import BinaryTree, Node
from collections import deque

def compute(tree):
    ret, deq = [], deque()
    deq.append(tree.root)

    while deq:
        cur_lvl, nxt_lvl = [], deque()
        while deq:
            node = deq.popleft()
            if node.left:
                nxt_lvl.append(node.left)
            if node.right:
                nxt_lvl.append(node.right)
            cur_lvl.append(node.data)

        ret.append(cur_lvl)
        deq = nxt_lvl

    return ret

if __name__ == '__main__':
    # Ugly but I'm building a binary tree here with depth 5
    # Letters and tree come from image in the epi book
    k = Node(1)
    k.left = Node(401)
    k.left.right = Node(641)
    k.right = Node(257)
    j = Node(2, right=k)
    i = Node(6, left=j)
    i.right = Node(271)
    i.right.right = Node(28)
    c = Node(271)
    c.left = Node(28)
    c.right = Node(0)
    f = Node(561)
    f.right = Node(3)
    f.right.left = Node(17)
    b = Node(6, left=c, right=f)

    root = Node(314, left=b, right=i)
    tree = BinaryTree(root)
    t = compute(tree)
    print(t)

    tree.add(971)
    t = compute(tree)
    print(t)
