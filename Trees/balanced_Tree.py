
def is_balanced(root):
    """
    Determine if a binary tree is height-balanced. A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one`
    :param root: TreeNode, the root of the binary tree
    :return: bool, True if the tree is height-balanced, False otherwise
    """

    def checkBalance(node):
        if not node:
            return 0
        left_height = checkBalance(node.left)
        if left_height == -1:
            return -1
        right_height = checkBalance(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    return checkBalance(root) != -1

