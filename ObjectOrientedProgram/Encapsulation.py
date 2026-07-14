"""#Create a class Employee with a private attribute __salary. Add a method raise_salary(percent) that increases salary only if percent > 0,
#and a get_salary() method to view it.
class Employee:
    def __init__(self, salary):
        self.__salary = salary 
    def raise_salary(self, percent):
        if percent > 0:
            self.__salary += self.__salary * percent / 100
        else:
            print("Percentage must be greater than 0.")
    def get_salary(self):
        return self.__salary
emp = Employee(50000)
print("Current Salary =", emp.get_salary())
emp.raise_salary(10)
print("Updated Salary =", emp.get_salary())
emp.raise_salary(-5)
print("Final Salary =", emp.get_salary())

#Try accessing __salary directly from outside the class — confirm it fails. Then access it via name mangling (obj._Employee__salary)— confirm it works. 
# Explain in your own words why Python allows this "back door."
class Employee:
    def __init__(self, salary):
        self.__salary = salary
emp = Employee(50000)
print(emp._Employee__salary)"""

#Create a class Temperature with a private __celsius. Add set_temp(value) that only accepts values above -273.15 (absolute zero),
#otherwise print "Invalid temperature". Add get_temp() to read it.
class Temperature:
    def __init__(self):
        self.__celsius = 0 

    def set_temp(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            print("Invalid temperature")

    def get_temp(self):
        return self.__celsius
t = Temperature()
t.set_temp(25)
print("Temperature:", t.get_temp())
t.set_temp(-300)
print("Temperature:", t.get_temp())