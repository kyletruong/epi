"""
Given a binary tree where each node contains an integer.
Find if a root-to-leaf path exists such that it equals the specified sum.
"""

def has_path(root, remaining_weight):
    """Solve using post-order traversal, process then recurse."""
    if not root:
        return False

    remaining_weight -= root.data
    # If leaf-node, check remaining_weight == 0
    if not root.left and not root.right:
        return remaining_weight == 0

    return (has_path(root.left, remaining_weight)
            or has_path(root.right, remaining_weight))
