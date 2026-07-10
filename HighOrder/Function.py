#Write a function to print "Hello World".
def Hello():
    print("hello world")
Hello()

#Write a function to print numbers from 1 to 10
def number():
    for i in range(0,11):
        print(i)
number()

#Write a function to add two numbers.
def add(a,b):
    sum = a+b
    print(sum)
add(5,10)

#Write a function to find the largest of two numbers.
def number():
    num1 = int(input("enetr the first number = "))
    num2 = int(input("enter the second number = "))
    if num1>num2:
        print(num1,"is largest")
    else:
        print(num2,"is largest")
number()

#Write a function to check whether a string is a palindrome.
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

word = input("Enter a string: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")