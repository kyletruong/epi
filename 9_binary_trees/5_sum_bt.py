# Compute the sum of binary numbers represented by the root-to-leaf paths

def sum_bt(root, partial_sum=0):
    if not root:
        return 0

    partial = partial_sum * 2 + root.data
    if not root.left and not root.right:
        return partial
    return sum_bt(root.left, partial) + sum_bt(root.right, partial)
