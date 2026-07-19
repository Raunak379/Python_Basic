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

#Build the LinkedList class above and create a list with values 1, 2, 3, 4, 5. Call display() to confirm it prints correctly.
class node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next

class SingleLL:
    def __init__(self,head=None):
        self.head = head
    def insert_value(self,value):
        temp = node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
    def printLL(self):
        t1 = self.head
        result = []
        while t1 is not None:
            result.append(t1.info)
            t1 = t1.next
        print(result)

obj = SingleLL()
obj.insert_value(1)
obj.insert_value(2)
obj.insert_value(3)
obj.insert_value(4)
obj.insert_value(5)
obj.printLL()

#Write a method length() that counts and returns the number of nodes in the list (without using any built-in length function — walk and count).
class Node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next

class SingleLL:
    def __init__(self,head = None):
        self.head = head
    def insertTheValue(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 =self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
    def printLL(self):
        t1 = self.head
        result = []
        while t1.next is not None:
            result.append(t1.info)
            t1 = t1.next
        print(result)
    def length(self):
        count = 0              
        t1 = self.head         

        while t1 is not None:  
            count += 1         
            t1 = t1.next       

        return count

obj = SingleLL()
obj.insertTheValue(1)
obj.insertTheValue(2)
obj.insertTheValue(3)
obj.insertTheValue(4)
obj.insertTheValue(5)
obj.printLL()
print(obj.length())