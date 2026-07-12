#Create a set of 3 fruits.
fruits = {"apple","banana","mango"}
print(fruits)

#Print all elements using a loop.
fruits = {"apple","banana","mango"}
for fruit in fruits:
    print(fruit)

#Remove duplicates from a list using a set.
num = [1,2,3,4,5,1,2,3]
result = set(dict.fromkeys(num))
print(result)

#Find the union of two sets.
set1 = {1,2,3,4}
set2 = {3,4,5,6}
union = set1|set2
print(union)

#Find the intersection  of two sets.
intersection = set1&set2
print(intersection)

#Find the difference between two sets.
diff = set1 - set2
print(diff)

#Find the symmetric difference of two sets.
sym = (set1-set2)| (set2-set1)
print(sym)

#Count the number of unique elements in a list.
num = [1,2,3,4,5,6,1,2,3,4]
count = len(set(num))
print(count)
#Convert a list into a set and back into a list.
num = [1,2,3,4,5,6,7]
set_num = set(num)
List_num = list(set_num)
print(num)
print(set_num)
print(List_num)

#Find common elements between two lists using sets.
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
set_num1 = set(list1)
set_num2 = set(list2)
common = set_num1&set_num2
print(common)

#Check whether one set is a subset of another.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))

#Check whether two sets are disjoint.
A = {1, 2, 3}
B = {3, 4, 5}
print(A.isdisjoint(B))