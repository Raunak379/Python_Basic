class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value
def preorder(root):
    if root != None:
        print(root.data, end = " ")
        preorder(root.left)
        preorder(root.right)
def Inorder(root):
    if root != None:
        Inorder(root.left)
        print(root.data, end = " ")
        Inorder(root.right)
def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = " ")

root = node(1)
root.left = node(3)
root.right = node(5)
root.left.left = node(2)
root.left.right = node(4)
root.right.right = node(8)
preorder(root)
Inorder(root)
postorder(root)