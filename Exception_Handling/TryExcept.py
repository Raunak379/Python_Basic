#Handle ZeroDivisionError.
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
    print("Type error")

#Use else with try-except.
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result =", result)

#Use finally to print "Program End".
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result =", result)
finally:
    print("Program End")

#Handle multiple exceptions in one program.
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("result = ",result)

#Raise a custom exception if age is less than 18
class InvalidAgeError(Exception):
    pass
age = int(input("Enter your age: "))
if age < 18:
    raise InvalidAgeError("Age must be 18 or above.")
else:
    print("You are eligible.")

#Write a program that safely divides two user-entered numbers.
try:
    num1 = float(input("enter the first number = "))
    num2 = float(input("enter the second number = "))
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("zero is not divisiual by any number")
except ValueError:
    print("invalid datatype value enter")