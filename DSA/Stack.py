#uses insert for push element
class stack:
    def __init__(self):
        self.lis = []
    
    def Length(self):
        return len(self.lis)

    def Push(self,value):
        self.lis.insert(0,value)
    
    def peek(self):
        if len(self.lis) == 0:
            raise Exception("stack is empty")
        else:
            return self.lis[0]
    def pop(self):
        if len(self.lis) == 0:
            raise Exception("stack is empty")
        else:
            return self.lis.pop(0)

stk = stack()
stk.Push(10)
stk.Push(20)
stk.Push(30)
stk.Push(40)

print(stk.peek())

print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())

#use append for pop
class Stack:
    def __init__(self):
        self.lis = []

    def Length(self):
        return len(self.lis)

    def Push(self, value):
        self.lis.append(value)

    def peek(self):
        if len(self.lis) == 0:
            raise Exception("Stack is empty")
        else:
            return self.lis[-1]

    def pop(self):
        if len(self.lis) == 0:
            raise Exception("Stack is empty")
        else:
            return self.lis.pop()


stk = Stack()

stk.Push(10)
stk.Push(20)
stk.Push(30)
stk.Push(40)

print(stk.peek())

print(stk.pop())    
print(stk.pop())    
print(stk.pop())    
print(stk.pop())    

