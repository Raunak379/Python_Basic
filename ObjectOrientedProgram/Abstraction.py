#Create an abstract class Employee with abstract methods calculate_salary() and job_title(). 
#Create two concrete subclasses Developer and Manager that each implement both differently.
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    @abstractmethod
    def job_title(self):
        pass
class developer(Employee):
    def __init__(self,monthly_salary):
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
    def job_title(self):
        return "developer"
class Manager(Employee):
    def __init__(self,monthly_salary,bonus):
        self.monthly_salary = monthly_salary
        self.bonus = bonus
    def calculate_salary(self):
        return self.monthly_salary + self.bonus
    def job_title(self):
        return "manager"
o1 = developer(50000)
o2 = Manager(70000, 15000)
print("Job Title:", o1.job_title())
print("Salary:", o1.calculate_salary())
print()
print("Job Title:", o2.job_title())
print("Salary:", o2.calculate_salary())

#Create an abstract class PaymentMethod with abstract method pay(amount). Create CreditCard and UPI subclasses, 
#each printing a different message when pay() is called. Then loop through a list of both objects calling .pay(500) on each
#— notice this combines abstraction and polymorphism together.
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")
class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")
credit = CreditCard()
upi = UPI()
payments = [credit, upi]
for payment in payments:
    payment.pay(500)
