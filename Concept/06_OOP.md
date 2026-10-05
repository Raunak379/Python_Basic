# Object-Oriented Programming (OOP)

OOP organizes code around **objects** — bundles of data (attributes) and behavior (methods) — instead of a flat sequence of functions and variables. Python's OOP rests on four pillars, each covered by one file in `ObjectOrientedProgram/`.

## Classes & Objects (`Class&Objects.py`)
A **class** is a blueprint; an **object** (instance) is a concrete thing built from that blueprint.

```python
class car:
    def __init__(self, brand, speed):   # constructor — runs automatically when you create an object
        self.brand = brand               # attribute, stored on THIS object
        self.speed = speed
    def show_info(self):                 # method — behavior tied to the object
        print("this car is a", self.brand, "going", self.speed, "km/h")

c1 = car("BMW", 100)   # object creation — calls __init__ automatically
c2 = car("jeep", 120)
```

### Why `self`?
`self` refers to **the specific object the method was called on**. `c1.show_info()` is really `car.show_info(c1)` under the hood — Python passes the object as the first argument automatically. This is how `self.brand` inside the method knows to look at `c1`'s brand and not `c2`'s — each object keeps its **own copy** of instance attributes, which is why `c1`'s and `c2`'s data never overlap (the second exercise in that file proves exactly this).

### Why `car.bark()` (calling on the class, not an object) fails
A regular method expects `self` (an object) as its first argument. Calling it on the class directly means there's no object to supply, so Python raises `TypeError: bark() missing 1 required positional argument: 'self'`.

## Encapsulation (`Encapsulation.py`)
Encapsulation = **hiding internal data**, exposing only controlled access through methods.

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary       # double underscore prefix → "private"
    def raise_salary(self, percent):
        if percent > 0:
            self.__salary += self.__salary * percent / 100
    def get_salary(self):
        return self.__salary
```
- `__salary` isn't *truly* private (Python has no hard privacy like Java), but Python performs **name mangling**: outside the class, `__salary` is actually stored as `_Employee__salary`. So `emp.__salary` fails (`AttributeError`), but `emp._Employee__salary` works — the "back door" your exercise explores. The point of encapsulation isn't unbreakable security, it's **signaling "don't touch this directly, use the methods"** and preventing *accidental* misuse — validation logic like `if percent > 0` only runs if people go through `raise_salary()` instead of poking the attribute directly.
- The `Temperature` example enforces a business rule (`value >= -273.15`, absolute zero) inside the setter — this is the real value of encapsulation: **centralizing validation** in one place instead of trusting every caller to check it themselves.

## Inheritance (`Inheritance.py`)
Inheritance lets a class **reuse and extend** another class's code.

```python
class vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def show_info(self):
        print("your vehicle name is", self.brand, "and also speed is", self.speed)

class car(vehicle):          # car IS-A vehicle
    def honk(self):
        print("brand name is", self.brand, "and also speed is", self.speed)
```
`car` automatically gets `__init__` and `show_info` from `vehicle` for free — it only needs to define what's *new* (`honk`).

### `super()`
```python
class Electric_car(car):
    def __init__(self, Brand, speed, Capacity):
        super().__init__(Brand, speed)   # runs the PARENT's __init__ first
        self.Capacity = Capacity          # then add the new attribute
```
`super().__init__(...)` calls the parent class's constructor so you don't have to retype `self.Brand = Brand; self.Speed = speed` — you reuse the parent's logic and only add what's new. This is the standard pattern whenever a child class needs *all* of the parent's setup plus a bit more.

### Overriding
```python
class car(vechical):
    def show_info(self):
        super().show_info()   # call parent's version too, then could add more after
```
"Overriding" means the child class defines a method with the **same name** as the parent's — when called on a child object, the child's version runs instead of the parent's. Calling `super().show_info()` inside the override lets you *extend* the parent's behavior rather than fully replacing it.

### Inherited-but-not-overridden methods
```python
class Vehicle:
    def fuel_type(self):
        print("Uses petrol or diesel.")
class Car(Vehicle):
    pass
Car().fuel_type()   # works! prints "Uses petrol or diesel."
```
If a child class doesn't define its own version of a method, Python walks up to the parent and uses *its* version — this upward lookup is called the **Method Resolution Order (MRO)**.

## Polymorphism (`Polymorphism.py`)
Polymorphism = "many forms" — **the same method call behaves differently depending on which object it's called on.**

```python
class circle(Shape):
    def Area(self): return 3.14 * self.r * self.r
class rectangle(Shape):
    def Area(self): return self.l * self.w

shapes = [circle(4), rectangle(5,5), triangle(4,4)]
for shape in shapes:
    print(shape.Area())   # calls a DIFFERENT Area() depending on the actual object type
```
The loop doesn't know or care whether `shape` is a circle or rectangle — it just calls `.Area()`, and Python dispatches to the correct class's implementation at runtime. This is **why** polymorphism is powerful: you write one loop that works for any shape, present or future, as long as it has an `Area()` method.

### Duck typing
```python
class printer:
    def start(self): print("printer machine is start")
class faxmachine:
    def start(self): print("fax machine is start")
def operate(device):
    device.start()   # works on ANY object with a .start() method — no shared parent class needed!
```
"If it walks like a duck and quacks like a duck, treat it like a duck." Python doesn't check types before calling a method — it just tries to call it. `operate()` works on *any* object that happens to have a `.start()` method, with zero inheritance relationship required. This is more flexible than languages that require a common interface/base class.

## Abstraction (`Abstraction.py`)
Abstraction = defining **what** a class must do, without saying **how**, forcing subclasses to fill in the details.

```python
from abc import ABC, abstractmethod
class Employee(ABC):              # ABC = Abstract Base Class
    @abstractmethod
    def calculate_salary(self):
        pass                       # no implementation — subclasses MUST provide one
```
- You **cannot create an object directly from `Employee`** (`Employee()` raises `TypeError: Can't instantiate abstract class`) — it exists purely as a contract.
- Any subclass (`developer`, `Manager`) **must** implement every `@abstractmethod`, or it will also be considered abstract and fail to instantiate.
- This combines with polymorphism in the `PaymentMethod` example: `CreditCard` and `UPI` both guarantee a `.pay(amount)` method exists (abstraction enforces the contract), and looping over `[credit, upi]` calling `.pay(500)` dispatches to each one's own version (polymorphism provides the different behavior).

## Class attributes vs. instance attributes (`Instance Attributes vs Class Attributes.py`)
```python
class BankAccount:
    bank_name = "HDFC"               # CLASS attribute — shared by ALL instances
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name   # INSTANCE attribute — unique per object
        self.balance = balance
```
- Class attributes live on the **class itself**, and every instance shares the *same* copy unless overridden.
- `Acc1.Bank_name = "sbi"` doesn't change the shared class attribute — it creates a **new instance attribute on `Acc1` only**, shadowing the class one just for that object. That's why `Acc2`/`Acc3`/`Bank.Bank_name` still print `"hdfc"` afterward, while `Acc1.Bank_name` prints `"sbi"`.
- The `Counter` example (`Counter.count += 1` inside `__init__`) relies on the fact that `Counter.count` is shared — every new object's constructor bumps the *same* shared counter, so after creating 5 objects, `Counter.count == 5`. This only works because the increment targets `Counter.count` (the class) explicitly, not `self.count` (which would instead create a separate per-instance attribute starting fresh each time).

## How to work with this topic
1. `self` = "the object this method was called on." Every instance method needs it as the first parameter.
2. Use `__init__` to set up what every object needs when it's created.
3. Reach for inheritance when one class is clearly a *more specific version* of another ("ElectricCar IS-A Car"); use `super()` to avoid repeating the parent's setup code.
4. Polymorphism means: write code against a *behavior* ("has an Area() / start() method"), not against a specific class — this is what makes OOP code extensible.
5. Use abstraction (`ABC` + `@abstractmethod`) when you want to **force** every subclass to implement certain methods, catching missing implementations at object-creation time instead of at a confusing runtime crash later.
6. Double-underscore attributes aren't unbreakable security — they're a convention that says "treat this as private," enforced loosely via name mangling.
