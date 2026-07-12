"""#Handle ZeroDivisionError.
try:
    num1 = 10
    num2 = 0
    print(num1/num2)
except ZeroDivisionError:
    print("cannot divided by zero")
print("program end")

#Handle ValueError when taking integer input.
try:
    age = int(input("enter the age = "))
    print("your age = ",age)
except ValueError:
    print("please enter number only")

#Handle IndexError while accessing a list.
num = [1,2,3]
try:
    print(num[5])
except IndexError:
    print("this index number is not exist")

#Handle KeyError while accessing a dictionary.
student = {"name":"raunak" ,"age" :21}
try:
    print(student["marks"])
except KeyError:
    print("marks does not exist")

#Handle TypeError when adding incompatible types.
num1 = 20
num2 = "20"
try:
    print(num1+num2)
except TypeError:
    print("Type error")"""

#Use else with try-except.
