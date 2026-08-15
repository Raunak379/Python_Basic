class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(root, value):
    if root is None:
        return Node(value)

    if root.data == value:
        return root

    if value < root.data:
        root.left = insert(root.left, value)

    else:
        root.right = insert(root.right, value)

    return root


def Search(root, value):
    if root is None:
        print("Element not Found")
        return

    if root.data == value:
        print("Element Found")
        return

    if value < root.data:
        Search(root.left, value)

    else:
        Search(root.right, value)


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

Search(root, 15)