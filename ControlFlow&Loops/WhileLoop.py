#print 1 to 5 number using while loop 
i = 1
while i<=5:
    print(i)
    i+=1

#print 5 to 1 reverse number print
i = 5
while i>=1:
    print(i)
    i-=1

#Count the number of digits in an integer.
number = int(input("enter the number"))
count = 0
while number>0:
    number //=10
    count +=1
    print(count)
