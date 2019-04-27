# Given a binary tree where each node contains an integer
# Find if a root-to-leaf path exists that == specified sum

def has_path(root, remaining_weight):
    if not root:
        return False

    # Top-down recursion (pre-order traversal) [process then recurse]
    remaining_weight -= root.data

    # If leaf-node, check that its sum == specified sum
    if not tree.left and not tree.right
        return remaining_weight == 0

    return (has_path(root.left, remaining_weight)
            or has_path(root.right, remaining_weight))
