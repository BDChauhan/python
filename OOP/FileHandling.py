# File Handling in Python
# why we need it - if we want some data to be stored permanent / to use it in future

f = open('F:\python\OOP\myData.txt', 'r')

# mode - read, write --> when you work on complext system, we need to give permission etc
# in read - we may achieve multithreading but in write - only one thread

# print(f.read())
print("line by line\n", f.readline())

f1 = open('abc', 'w')
f1.write("This is written into 'abc' from FileHandling program.")
# print(f1.read())
f1.close()

# copy data of f into f1
f1 = open('abc', 'a')
for data in f:
    f1.write(data)

