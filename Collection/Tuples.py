#Create a tuple of 5 fruits.
fruits = ("apple","Banana","Watermelon","mango","plum")
print(fruits)

print(fruits[-1::],fruits[:1])#Print the first and last element.

print(fruits[3])#Print the third element.

print(len(fruits))#Print the length of the tuple.

print("apple" in fruits) #Check if "Apple" exists in the tuple.

index = fruits.index("Banana")
print(index)#Find the index of "Banana".

for i in range(len(fruits)):
    print(fruits[i]) #Print all elements using a loop.

print(fruits[::-1]) #Reverse a tuple using slicing.

print(fruits[::2])#Print every second element.

new_list = list[fruits]
print(new_list)# Convert a tuples into a list

#Count how many times 10 appears in a tuple.
num = (10,20,30,40,10,35,10)
count = num.count(10)
print(count)

#Create a nested tuple and access an inner element.
num = (
    (1,2),
    (2,3),
    (4,9),
    (7,6)
)
print(num[1][1])

#Find the largest value in a tuple without using max().
number = (32,84,44,94,35,65)
largest = number[0]
for i in range(len(number)):
    if largest < number[i]:
        largest = number[i]
print(largest)

#Unpack a tuple into separate variables.
num = (1,2,3,4)
a,b,c,d = num
print(a)
print(b)
print(c)
print(d)