# Given a binary tree where each node contains an integer
# Find if a root-to-leaf path exists that == specified sum

# Solve using post-order traversal, process then recurse
def has_path(root, remaining_weight):
    if not root:
        return False

    remaining_weight -= root.data
    # If leaf-node, check remaining_weight == 0
    if not root.left and not root.right
        return remaining_weight == 0

    return (has_path(root.left, remaining_weight)
            or has_path(root.right, remaining_weight))
