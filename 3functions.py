# calling function by passing value = pass by value/call by value (both will share same id - but moment we ll change value, it will change id)
# passing the address  = call/pass by ref
# but python is "Pass by object reference" (obj ref are passed by value)
# see last function here

# formal args - args when defining fun
# actual args - args when calling fun - 
#     1. position args (a,b) --> (2,3) - maintain seq
#     2. Keyword args (a,b) --> (a=2, b=3)
#     3. default value (a,b=12) --> (2)
#     4. variable length args (a, *b) --> (2,3,4,5) here b = (3,4,5)
    
def totalSnacks (snacks):
    print(f"you have {snacks} type of snacks!!")

def addSnacks(snacks, extraSnacks):
    print(f"you added {extraSnacks} snacks extra")
    print(f"total snacks after addition : {snacks+extraSnacks}")

def mathFun(arg1 ,arg2):
    print("mul", arg1*arg2)
    print("div", arg1/arg2)
    print("abs div", arg1//arg2)
    print("mod", arg1%arg2)
    

    
print("function checking by passing value 5")
totalSnacks(5)
addSnacks(5,2)
mathFun(7,2)

def userInput():
    print("enter your name:")
    name = input()
    print("age?")
    age = int(input())
    print("so you say your name is", name)
    print("and you will be of", age+5, "after five years")

userInput()

# function returning value
def retSum(a,b):
    return a+b

print("sum of 5 + 2 =",retSum(5,2))

# pass by object ref

def update(x):
    print("id of x",id(x))
    x = 10
    print("x",x)
    
print("before calling function")
a = 11
print("id of a",id(a))
print("a",a)
update(a)
print("after calling function")
print("a", a)

# id would be same so it is not call by value
# printiing id of x after changing value

def update(x):
    print("id of x",id(x))
    x = 10
    print("id of x after changing value",id(x))
    print("x",x)
    
print("before calling function")
a = 11
print("id of a",id(a))
print("a",a)
update(a)
print("after calling function")
print("a", a)
print("id of a", id(a))

# moment you change value, id would be changed - reason---> here 'int' is immutable so new id
# if you will try with 'list' --> then id would not be changed

