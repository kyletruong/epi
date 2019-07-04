# Compute the sum of binary numbers represented by the root-to-leaf paths
# Root-to-leaf represented as binary string e.g. 100110

# Solve using post-order traversal, process then recurse
def sum_bt(root, partial_sum=0):
    if not root:
        return 0

    partial = partial_sum * 2 + root.data
    # If leaf-node 
    if not root.left and not root.right:
        return partial

    return sum_bt(root.left, partial) + sum_bt(root.right, partial)
