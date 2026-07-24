class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.items = [None]*size
        self.front = self.rear = -1
    def insert(self,value):  #enqueue
        if (self.rear+1) % self.size == self.front: #check full or not
            print("queue is full")
        elif self.front == -1:   #check Q is empty or not
            self.front = self.rear = 0 #rear or front at same postion 0 index
            self.items[self.rear] = value #insert the value at 0 index that mean rear or front are same postion, or only insertion is in rear position so that is called self.rear use
        else:
            self.rear = (self.rear  + 1) % self.size # normal insertion if some index are covered or some are empty this logic can use
            self.items[self.rear] = value
    def delection(self):  #dequeue   
        if self.front == -1: # check empty or not
            print("queue is empty")
        elif self.front == self.rear: #only one element present that mean ham usee empty karde
            print(self.items[self.front]) #delete element printed
            self.front = self.rear = -1 # this logic mean empty this queue
        else: 
            print(self.items[self.front]) # print deleted element
            self.front = (self.front + 1)% self.size #normal delection logic some index value are present and some are deleted

cq = CircularQueue(5)
cq.insert(10)
cq.insert(20)
cq.insert(30)
cq.insert(40)
cq.insert(50)

cq.insert(60) #queue is full

cq.delection() #delete 10

cq.insert(60) #After delection they can insert 60
cq.delection()#20
cq.delection()#30
cq.delection()#40
cq.delection()#50
cq.delection()#60
cq.delection() #queue is empty
