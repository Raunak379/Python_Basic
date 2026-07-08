#square number
def Square(x):
    return x*x
numbers = [1,2,3,4,5]
print(list(map(Square,numbers)))

#Convert ["1", "2", "3", "4"] into integers.
numbers = ["1", "2", "3", "4"]
print(list(map(int,numbers)))

#Convert ["python", "java", "c++"] into uppercase.
str = ["python", "java", "c++"]
print(list(map(lambda x:x.upper(),str)))

#Add two lists using map().
List1=[1,2,3]
list2=[4,5,6]
Add = lambda x,y:x+y
print(list(map(Add,List1,list2)))

#Find the cube of every number using a lambda function.
Numbers = [1,2,3,4,5]
cube = lambda x:x**3
print(list(map(cube,Numbers)))