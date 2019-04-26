# Given p and q, find their least common ancestor
# Nodes have a parent field

def lca(p, q):
    def height(node):
        ht = 0
        while node.parent:
            node = node.parent
            ht += 1
        return ht

    p_ht, q_ht = height(p), height(q)
    diff = abs(p_ht - q_ht)

    if q_ht > p_ht:
        p, q = q, p

    for _ in range(diff):
        p = p.parent

    while p is not q:
        p, q = p.parent, q.parent

    return p
