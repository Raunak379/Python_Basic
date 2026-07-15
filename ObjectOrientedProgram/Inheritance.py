#Create a parent class Vehicle with __init__(self, brand, speed) and a method show_info().
#Create a child class Car that inherits from Vehicle and adds a method honk().
class vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def show_info(self):
        print("your vechicle name is", self.brand, "and also speed is", self.speed)
class car(vehicle):
    def honk(self):
        print("brand name is", self.brand, "and also speed is", self.speed)
c1 = car("BMW",50)
c1.honk()

#Create a child class ElectricCar(Car) that adds a battery_capacity attribute. Use super().
#__init__() correctly to set up brand, speed, and the new attribute in one __init__.
class car:
    def __init__(self,Brand,speed):
        self.Brand = Brand
        self.Speed = speed
class Electric_car(car):
    def __init__(self,Brand,speed,Capacity):              ###uses of super key
        super().__init__(Brand,speed)
        self.Capacity = Capacity
    def display(self):
        print("Brand",self.Brand)
        print("speed",self.Speed)
        print("capacity",self.Capacity,"kwh")
o1 = Electric_car("bmw",40,6)
o1.display()

#Override show_info() in Car so it prints the parent's info plus an extra line saying "This is a car." (use super()).
class vechical():
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    def show_info(self):
        print("your vechicle name is", self.name, "and also speed is", self.speed)   ##(override use)
class car(vechical):
    def show_info(self):
        super().show_info()
c1 = car("bmw",100)
c1.show_info()

#Predict without running: if Vehicle has a method fuel_type() and Car does NOT override it, 
# what happens when you call .fuel_type() on a Car object? Why?
class Vehicle:
    def fuel_type(self):
        print("Uses petrol or diesel.")
class Car(Vehicle):
    pass
car = Car()
car.fuel_type()