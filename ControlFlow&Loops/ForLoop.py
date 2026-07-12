#print number 1 t0 5 using for loop
for i in range(1,6):#range function is used to sequence of numbers.
    print(i)


#print your name 5 times.
for i in range(6):
    print("raunak")

#range = start,stop,step
for i in range(0,20,2):
    print(i)

#Print even numbers from 1 to 20
for i in range(1,21):
    if i%2 == 0:
        print(i)

#Find the sum of numbers from 1 to 100.
sum = 0
for i in range(1,101):
    sum += i
    print(sum)

#Find the factorial of a number.
number = int(input("enter the number"))
factorial = 1
for i in range(1,number+1):
    factorial *= i
    print(factorial)

#Print the multiplication table of a given number.
num = int(input("enter the number : "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#pattern Question
row = 5
for i in range(1,row+1):
    for j in range(i):
        print("*",end="")
    print()

#square of number in pattern
num = 4
for i in range(1,num+1):
    for j in range(1,num+1):
        print(j,end="")
    print()