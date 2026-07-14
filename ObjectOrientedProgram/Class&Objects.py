#Create a class Car with attributes brand and speed. Add a method show_info() that prints "This car is a <brand> going <speed> km/h".
class car:  # class 
    def __init__(self,brand,speed): #constructor
        self.brand = brand #variable define
        self.speed = speed #variable define
    def show_info(self): #method
        print("this car is a ", self.brand , "going ", self.speed , "km/h")

c1 =car("BMW", 100) #object creaction
c2 =car("jeep", 120)

c1.show_info() #call methods
c2.show_info()

#Create two Car objects with different values and call show_info() on both. Confirm their data doesn't overlap.
class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def show_info(self):
        print("Brand = ", self.brand)
        print("year = ", self.year)
        print("model", self.model)

c = car("BMW","x7",2026)
c.show_info()

#Predict without running: What happens if you try Dog.bark() (calling on the class, not an object)? Why does it fail?
class dog:
    def __init__(self,bread):
        self.bread = bread
    def info(self):
        print("bread", self.bread)

d = dog("rotwiller")
d.info()               # it will rise typerror if you calling class not an object

#Create a class Student with name and marks. Add a method is_pass() that returns True if marks >= 40, else False.
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def Is_pass(self):
        if self.marks >= 40:
            print(self.name,"pass",True)
        else:
            print(self.name,"fail",False)
s1 = student("Raunak",30)
s2 = student("himanshi",50)
s1.Is_pass()
s2.Is_pass()