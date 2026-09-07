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
def get_successor(root):
    root = root.right
    while root != None and root.left != None:
        root = root.left
    return root
def delete(root,value):
    if root is None:
        return root
    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.left = delete(root.right,succ.data) 
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

delete(root,30)
print("\n")
Inorder(root)