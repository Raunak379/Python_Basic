#Create a parent class Shape with a method area() that returns 0. 
#Create child classes Circle, Rectangle, and Triangle, each overriding area() with its own correct formula (accept dimensions via __init__).
class Shape:
    def Area(self):
        return 0
class circle:
    def __init__(self,r):
        self.r = r
    def Area(self):
        return 3.14*self.r*self.r
class rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def Area(self):
        return self.l*self.w
class triangle:
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def Area(self):
        return 0.5*self.b*self.h
o1 = circle(4)
print(o1.Area())
o2 =rectangle(5,5)
print(o2.Area())
o3 = triangle(4,4)
print(o3.Area())

#Put one object of each shape into a list, loop through it, and print each one's area() — using one single loop, no if/elif checks.
class Shape:
    def Area(self):
        return 0
class circle(Shape):
    def __init__(self,r):
        self.r = r
    def Area(self):
        return 3.14*self.r*self.r
class rectangle(Shape):
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def Area(self):
        return self.l*self.w
class triangle(Shape):
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def Area(self):
        return 0.5*self.b*self.h


o1 = circle(4)
o2 =rectangle(5,5)
o3 = triangle(4,4)
shapes = [o1,o2,o3]
for Shape in shapes:
    print(Shape.Area())

#Using duck typing (no shared parent class at all), create two unrelated classes Printer and FaxMachine, both with a method start().
#Write one function operate(device) that calls device.start() and works on both.
class printer:
    def start(self):
        print("prinert machine is start")
class faxmachine:
    def start(self):
        print("fax machine is start")
def operate(device):
    device.start()
printer = printer()
fax = faxmachine()

operate(printer)
operate(fax)