#Print the first three characters.
word = "Programming"
print(word[0:3])

#Print the last three characters.
word = "programming"
print(word[-3:]) #last three digit print

#Print everything except the first character, and last, and first or last
word = "programming"
print(word[1:]) #first
print(word[:-1]) #last
print(word[1:-1]) #first and last

#Print every second character.
word = "Programming"
print(word[::2]) # every 2nd element
print(word[::3]) # every 3rd element

#Reverse the string using slicing.
word = "Programming"
print(word[::-1]) #Reverse

#Print the string in reverse, skipping one character.
word = "Programming"
print(word[::-1][::2])

#Print the last four characters.
word = "Programming"
print(word[-4:])

#Reverse only the last five characters.
word = "programming"
print(word[-5:][::-1])

#Print everything except the first two elements.
word = "programming"
print(word[0:11][2:])

#Extract the word "Python".
text = "I Love Python Programming"
print(text[7:13])

#Reverse only "Python".
text = "I Love Python Programming"
print(text[7:13][::-1])

#Extract every alternate character from:

word = "ABCDEFGHIJK"
print(word[::2])
