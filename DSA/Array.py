# use array module
import array
val = array.array('i',[1,2,3,4,5,6])
for i in range(0,6):
    print(val[i],end = " ")

#using * in array
from array import *
val = array('i',[1,2,3,4,5,6])
for i in range(0,6):
    print(val[i],end = " ")

#reverse use
from array import *
val = array('i',[1,2,3,4,5,6])
val.reverse()
for i in range(0,6):
    print(val[i],end = " ")

#insert and append numbeer
from array import *
val = array('i',[1,2,3,4,5,6])
val.insert(1,50)
val.append(100)
for i in range(0,6):
    print(val[i],end = " ")

#replace
from array import *
val = array('i',[1,2,3,4,5,6])
val[2] = 200
for i in range(0,6):
    print(val[i],end = " ")

#transfer one array element to another
from array import *
val = array('i',[1,2,3,4,5,6])
copyArray = array(val.typecode,(x for x in val))
for i in range(0,6):
    print(copyArray[i],end = " ")

#delete element
from array import *
val = array('i', [1, 2, 3, 4, 5, 6])
val.pop(3)  
for i in range(len(val)):
    print(val[i], end=" ")

#remove element
from array import *
val = array('i', [1, 2, 3, 4, 5, 6])
val.remove(3)
for i in range(len(val)):
    print(val[i], end=" ")

#indexing of array
from array import *
val = array('i', [1, 2, 3, 4, 5, 6])
abc = val[1:4]
print(abc)

#user input
from array import *
arr = array('i',[])
n = int(input("enter a number = "))
for i in range(0,n):
    arr.append(int(input("enter next input = ")))
for x in arr:
    print(x,end= " ")

#search element
from array import *
val = array('i',[1,2,3,4,5,6])
i = val.index(4)
print(i)

#numpy uses
from numpy import *
val = array([1,2,3,4.5,'a'])
for x in val:
    print(x,end=" ")

#linspace
from numpy import *
val = linspace(10,20,5)
for x in val:
    print(x,end=" ")

#arange
from numpy import *
val = arange(10,20,2)
for x in val:
    print(x,end=" ")

#zero 
from numpy import *
val = zeros(10)
for x in val:
    print(x,end=" ")

#ones
from numpy import *
val = ones(10)
for x in val:
    print(x,end=" ")

#Full
from numpy import *
val = full(10,5)
for x in val:
    print(x,end=" ")

#one -d-  array ,two -d- array
from numpy import *
one = array([1,2,3,4,5])
print(one)
two = array([[1,2,3],[4,5,6],[7,8,9]])
print(two)

#three -d- array
from numpy import *
three = array([[[1,2],[3,4],[5,6],[7,8]]])
print(three)