# exercise 29, 30, 31

# logical op - 'and' 'or' 'not' '==' '!=' '>=' '<=' 'True' 'False'

a = 1
b = 0

print(a>b)
print(a<=b)
print(a==b)
print(a or b)
print(a and b)
print(True == a)
print(True == b)
print(b == True)

# so python considers 1 as true and 0 as false!

# lets add if else statements

print("input a:")
a=input()

print("input b:")
b=input()

print("input c:")
c=input()

if(a>b):
    print("a is greater than b")
else:
    print("b is greater than a")
    
if(a>b and a>c):
    print("a is greater than b,c")
elif(a>b and a<c):
    print("c is greater than a,b")
elif(a<b and a<c):
    if(b>c):
        print("b is greater than a,c")
    else:
        print("c is greater than a,b")
else:
    print("a,b,c are same")