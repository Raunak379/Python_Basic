#Find the sum of [5, 10, 15, 20]
from functools import reduce

numbers = [5, 10, 15, 20]
print(reduce(lambda x,y:x+y,numbers))



#Find the product of [1, 2, 3, 4, 5].
from functools import reduce
def Multiply(x,y):
    return x*y
numbers = [1, 2, 3, 4, 5]
print(reduce(Multiply,numbers))



#Find the largest number in [45, 12, 89, 34, 67]
from functools import reduce
def largest(x,y):
    return x if x>y else y
numbers = [45, 12, 89, 34, 67]
print(reduce(largest,numbers))




#Find the smallest number in [45, 12, 89, 34, 67].
from functools import reduce 
numbers = [65,74,46,66,12,78]
Smallest = lambda x,y:x if x<y else y
print(reduce(Smallest,numbers))



#Join ["I", "love", "Python"] into one sentence.
from functools import reduce

def word(x,y):
    return x+ " " +y
sen = ["i", "love", "python"]
print(reduce(word,sen))