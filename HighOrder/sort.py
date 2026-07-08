#Sort [15, 2, 30, 8, 21] in ascending order.
numbers = [15,2,30,8,21]
print(sorted(numbers))

#Sort the same list in descending order.
numbers = [15,2,30,8,21]
print(sorted(numbers,reverse=True))

#Sort ["cat", "elephant", "dog", "lion"] by length.
animals = ["cat", "elephant", "dog", "lion"]
def length(x):
    return len(x)
print(sorted(animals,key=length))

#Sort students by marks using lambda
students = [("Raunak",85), ("Himanshu",90), ("ankit",47), ("mehak",84)]
sort = lambda x:x[1]
print(sorted(students,key=sort))

#Sort numbers based on their last digi
def lastDigit(x):
    return x%10
number = [25,12,43,56,87,99]
print(sorted(number,key=lastDigit))