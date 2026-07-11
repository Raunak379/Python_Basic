#Create a list of 5 fruits.
Fruits = ["apple", "banana", "orange", "grapes", "mango"]
print(Fruits)

#print first element
print(Fruits[0])

#print last element
print(Fruits[4])

#change the 4th element
Fruits[3] = "kiwi"
print(Fruits)

#Add "Watermelon" using append()
Fruits.append("Watermelon")
print(Fruits)

#Insert "Grapes" at index 2
Fruits.insert(2,"grapes")
print(Fruits) 

#Reverse a list.
print(Fruits[::-1])

#Sort numbers in ascending order.
number = [24,54,23,98,86,56]
number.sort()
print(number)

#Sort numbers in descending order.
number = [24,54,23,98,86,56]
number.sort(reverse=True)
print(number)

#Count how many times 10 appears in a list.
num = [10,56,76,10,10]
count = num.count(10)
print(count)
for i in range(len(num)):
    if num[i] == 10:
        count += 1
        print(i)

#Find the largest element without using max().
num = [35,64,75,45,89]
larg = num[0]
for i in range(len(num)):
    if num[i] > larg:
        larg = num[i]
print(larg)

#Find the smallest element without using min().
num = [78,56,34,86,79]
small = num[0]
for i in range(len(num)):
    if small > num[i]:
        small = num[i]
print(small)

#Find the second largest element.
num = [10,65,5,98,8]
large = num[0]
Seclarge = num[0]
for i in range(len(num)):
    if large < num[i]:
        larg = num[i]
for i in num:
    if i > Seclarge and  i != larg:
        Seclarge = i
print(Seclarge)


#Remove duplicate elements.
#method -1 
numbers = [1, 2, 2, 3, 4, 4, 5, 1]

unique = []

for i in range(len(numbers)):
    found = False

    for j in range(len(unique)):
        if numbers[i] == unique[j]:
            found = True
            break

    if found == False:
        unique.append(numbers[i])

print(unique)

#method -2 
numbers = [1, 2, 2, 3, 4, 4, 5, 1]

unique = []

for i in range(len(numbers)):
    if numbers[i] not in unique:
        unique.append(numbers[i])

print("Original List:", numbers)
print("List after removing duplicates:", unique)

#method -  3
lst = [1, 2, 2, 3, 4, 4, 5]
result = list(dict.fromkeys(lst))
print(result) 

#merge two lists.
lis1 = [1,2,3,4,5]
lis2 = [6,7,8,9,10]
merge_list = lis1+lis2
print(merge_list)

#Reverse a list without using reverse().
list = [1,2,3,4,5,6]
reverse = list[::-1]
print(reverse)

#Check whether an element exists in a list.
list = [1,2,3,4,5]
print(3 in list)

#Find the sum of all elements in a list.
from functools import reduce
def add(x,y):
    return x+y
num = [1,2,3,4,5,6]
arr =reduce(add,num)
avg = arr/len(num)
print(arr)
print(avg)#Find the average of all elements.

#Separate even and odd numbers into two different lists.
num = [10,24,33,42,57,68,77,18,91]
even = []
odd = []
for i in range(len(num)):
    if num[i] % 2 == 0:
        even.append(num[i])
    else:
        odd.append(num[i])
print("even number = ",even)
print("odd number = ",odd)