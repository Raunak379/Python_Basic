class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(root, value):
    # If tree/subtree is empty
    if root is None:
        return Node(value)

    # If value already exists
    if root.data == value:
        return root

    # Insert in left subtree
    if root.data > value:
        root.left = insert(root.left, value)

    # Insert in right subtree
    else:
        root.right = insert(root.right, value)

    return root


def Inorder(root):
    if root is not None:
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)


root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)

Inorder(root)

