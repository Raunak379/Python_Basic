#Starts from 0 and moves left to right.
Name = "Raunak"
print(Name[0])
print(Name[1])

#Access First and Last Character
name = "Raunak"
print(name[0])
print(name[-1])

#if you access an index that doesn't exist, Python raises an error.
name = "raunak"
print(name[1])

#Print all even-index characters.
word = "Programming"
for i in range(0,len(word),2):
    print(word[i])

#Print the second element.
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[1])

#Replace the first element.
numbers = [10, 20, 30]
numbers(0)=100
print(numbers)


#Find the smallest character (alphabetically) using indexing.
word = "python"
smallest = "p"
for i in range(1,6):
    if smallest>word[i]:                #################################################
        smallest = word[i]
print(smallest)

#Print each character with its index.
word = "Python"
for i in range(0,6):
    print(i,word[i])

#Find how many times 'a' appears using indexing.
word = "banana"
count = 0
for i in range(0,len(word)):
    if word[i] == 'a':
            count +=1 #count = count +1
print(count)