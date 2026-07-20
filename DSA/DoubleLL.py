#InserAtEnd
class Node:
    def __init__(self,value = None):
        self.data = value
        self.prev = None
        self.next = None
class DoubleyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return 
        t = self.head
        while t.next is not None:
            t = t.next
        
        t.next = temp
        temp.prev = t
    
    def printDLL(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = DoubleyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.printDLL()

#insertATBeg
class Node:
    def __init__(self,value = None):
        self.data = value
        self.prev = None
        self.next = None
class DoubleyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return 
        t = self.head
        while t.next is not None:
            t = t.next
        
        t.next = temp
        temp.prev = t
    def insertAtBeg(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def printDLL(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = DoubleyLL()
obj.insertAtBeg(5)
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.printDLL()
    
    