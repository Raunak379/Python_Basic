#Create a dictionary with name, age, and city.
dict = {"name":"Raunak", "age":21, "city":"Siwan"}
print(dict)

#print the value of name.
print(dict.get("name"))

#modify the name 
dict["name"] = "Ankesh"
print(dict)

#Add a new key course.
dict["course"] = "bca"
print(dict)

#Remove city
dict.pop("name")
print(dict)

#Print all keys.
for key in dict:
    print(key)

#Print all values.
for value in dict.values():
    print(value)

#Print all key-value pairs.
for key,value in dict.items():
    print(key ,":", value)

#Check whether "age" exists.
print("age" in dict)

#Find the length of the dictionary.
length = len(dict)
print(length)

#Create a nested dictionary.
students ={
    "student1":{"name":"Raunak","age":21,"city":"Siwan"},
    "student2":{"name":"Himanshi","age":20,"city":"haldwani"}
}
print(students)

#Merge two dictionaries using update()
dict1 = {"name": "Raunak","age": 21}
dict2 = {"age": 25,"city": "Delhi"}
dict1.update(dict2)
print(dict1)

#Count the frequency of each character in a string using a dictionary.
text = "programming"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

#Find the student with the highest marks from a dictionary.
#method 1
marks = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 88,
    "Neha": 95
}

highest_student = ""
highest_marks = 0

for student in marks:
    if marks[student] > highest_marks:
        highest_marks = marks[student]
        highest_student = student

print("Student with highest marks:", highest_student)
print("Highest marks:", highest_marks)

#method 2
marks = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 88,
    "Neha": 95
}

student = max(marks, key=marks.get)

print("Highest Student:", student)
print("Marks:", marks[student])

#Reverse keys and values in a dictionary.
student = {
    "name": "Raunak",
    "course": "BCA",
    "city": "Delhi"
}
reversed_dict = {}
for key, value in student.items():
    reversed_dict[value] = key
print(reversed_dict)