#even Number
def even(x):
    return x % 2 == 0
Numbers = [1,2,3,4,5]
print(list(filter(even, Numbers)))



#Keep only numbers greater than 20 from[10, 25, 30, 15, 40]. using lambda lunction
Numbers = [10,25,30,40,15]
print(list(filter(lambda x:x >20,Numbers)))



#Filter all negative numbers from [-5, 3, -2, 7, 0]
def negative(x):
    return x < 0
Numbers = [-5, 3, -2, 7, 0]
print(list(filter(negative,Numbers)))



#Keep only words that start with the letter "P" from ["Python", "Java", "PHP", "C"]
def StartswitchP(x):
    return x.startswith("P")
Letters = ["Python", "Java", "PHP", "C"]
print(list(filter(StartswitchP,Letters))) #####Startswitch



#Remove all empty strings from ["Hi", "", "Python", "", "AI"].
def empty(x):
    return x == ""
Letters = ["Hi", "", "Python", "", "AI"]
print(list(filter(empty,Letters)))



#Filter all numbers divisible by 3 from range(1, 21).
number = range(1,21)
print(list(filter(lambda x:x%3 == 0,number)))