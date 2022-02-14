# from cmath import log, sin
# from math import sqrt
from numpy import *
import numpy

num = array([1,2,3,4])

print(type(num))
print(num.dtype)

num1 = linspace(2,10,3) # will return float coz we are divinding in some parts defaukt num of parts = 50
print(num1)

num1 = arange(2,10,3)
print(num1)

num1 = logspace(2,10,3) # starts from 10^2, ends 10^10 divides in 3 parts 
print(num1)

num1 = zeros(5)
print(num1)

num1 = ones((5,5),int)
print(num1)


# operations on array in numpy

arr = array([1,5,3,7,2])

arr = arr +5
print(arr)

arr1 = ([2,3,5,2,1]) 
print(arr+arr1) #vectorized operation

print(sin(arr))
print(log(arr))
print(sqrt(arr))
print(numpy.sinc(arr))
print(numpy.sqrt(arr))
print(min(arr))
print(sort(arr))

arr2 = arr #we still have one array, arr2 will only point to arr = shallow copy
print(id(arr),id(arr2))

arr[1]= 55
print(arr2) # values are changing for both

# to create new arr wth diff address
arr2 = arr.view() # on diff location but still shallow copy
print(id(arr),id(arr2))

arr[1]= 66
print(arr2)

arr2 = arr.copy() # on diff location, deep copy
print(id(arr),id(arr2))

arr[1]= 77
print(arr)
print(arr2)
