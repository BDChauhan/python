# all values of same type (unlike list)
# dont have spacific size - shrink or expand it!
# need to specify proper typecode (b/B/u/h/H/i/I/l/L/f/d)
# cannot work with multi dimentional array

import array as arr
from tabnanny import check

num = arr.array('i',[1,2,3,7])
print(type(num))

# num = arr.array('b',[1,2,3,4,5]) signed char, B-unsigned char (1 byte)
# u - unicode char (2 bytes)
# short - h,H int - i,I long - l,L (2 bytes) 
# f - float - 4 bytes
# d - double - 8 bytes

charArr = arr.array('u',['a','b','c',"d"])
print(type(charArr))
print(charArr)

# num.buffer_info() will give size of arr in form of (address,size)
print(num.buffer_info())
num.reverse()
print(num)

for i in num:
    print(i)

print()

for i in range(len(charArr)):
    print(charArr[i])
    
# create new arr with help of existing array

newNum = arr.array(num.typecode, (a*2 for a in num) )
print(num)
print(newNum)
num[2] = 12
print(num)
num.append(2)
print(num)
num.remove(1)
print(num)

# how to delete element at specific index