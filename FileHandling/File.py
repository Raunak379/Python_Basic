#Create a file named student.txt.
file = open("student.txt", "w")
file.close()
print("File 'student.txt' created successfully.")

#Write your name to the file.
file = open("student.txt","w")
file.write("Raunak")
file.close()
print("name weitten to the file successfully")

#Read and print the file contents.
file = open("student.txt","r")
content = file.read()
print(content)
file.close()

#Append your city to the file.
file = open("student.txt", "a")
append = file.write("\nSiwan")
file.close()
print("city append successfuly")

#Count the number of lines in a file.
file = open("student.txt","r")
content = file.readlines()
print("length of line = ", len(content))
file.close()

#Read a file line by line.
file = open("student.txt","r")
content = file.readlines()
print(content)
file.close

#Copy the contents of one file to another.
source_file = open("student.txt","r")
destinsation_file = open("copied.txt","w")
content = source_file.read()
destinsation_file.write(content)
source_file.close()
destinsation_file.close()
print("another file is created and copy data form source file")

#Count the number of words in a file.
file = open("student.txt","r")
content = file.read()
word = content.split()
print("number of word = ",len(word))
file.close()

#Count the number of characters in a file.
file = open("student.txt", "r")
content = file.read()
print("Number of characters:", len(content))
file.close()

#Search for a word in a file.
file = open("student.txt", "r")
content = file.read()
word = input("enter the word = ")
if word in file:
    print("word found")
else:
    print("word not found")
file.close()

#Merge two text files.if file is not found the they create error so, use error handling
try:
   file1 = open("file1.txt", "r")
   file2 = open("file2.txt", "r")
   merged = open("merged.txt", "w")
   merged.write(file1.read())
   merged.write("\n")
   merged.write(file2.read())
   file1.close()
   file2.close()
   merged.close()
   print("Files merged successfully.")
except FileNotFoundError:
   print("file is not found")