#insertAtEnd
class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next
class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
    def printerLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.info)
            t1 = t1.next
obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.printerLL()

#insertAtBeg
class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next
class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
    def insertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def printerLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.info)
            t1 = t1.next
obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.printerLL()

#insertAtMid
class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next
class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    def insertAtMid(self, value, x):
        temp = Node(value)
        t1 = self.head
        while t1 is not None:
            if t1.info == x:
                temp.next = t1.next
                t1.next = temp
                break
            t1 = t1.next
    def printerLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.info)
            t1 = t1.next
obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtMid(40, 20)
obj.printerLL()

#delete element
class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next
class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    def insertAtMid(self, value, x):
        temp = Node(value)
        t1 = self.head
        while t1 is not None:
            if t1.info == x:
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next
        print("Value", x, "not found.")
    def deleteLL(self, value):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.info == value:
            self.head = self.head.next
            return
        prev = None
        t1 = self.head
        while t1 is not None:
            if t1.info == value:
                prev.next = t1.next
                return
            prev = t1
            t1 = t1.next
        print("Value", value, "not found.")
    def printerLL(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        t1 = self.head
        while t1 is not None:
            print(t1.info, end=" -> ")
            t1 = t1.next
        print("None")
obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtMid(40, 20)
obj.deleteLL(30)
obj.printerLL()