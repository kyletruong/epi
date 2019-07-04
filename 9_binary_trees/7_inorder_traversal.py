# Implement in-order traversal on a binary tree iteratively

def inorder(root):
    stack, result = [], []

    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            result.append(root)
            root = root.right

    return result
