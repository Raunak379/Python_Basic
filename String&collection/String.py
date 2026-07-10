#Print the first character.
word = "Python"
print(word[0]) #First Element
print(len(word)) #length

#Print every character using a loop.
word = "Python"
for i in range(len(word)):
    print(word[i])

#Print characters in reverse order using a loop.
word = "Python"
for i in range(5,-1,-1):
    print(word[i])

#Count the number of characters without using len().
word = "Programming"
count = 0
for ch in word:
    count = count + 1
print(count)

#Print all characters with their index.
Word = "python"
for i in range(6):
    print(i,word[i])