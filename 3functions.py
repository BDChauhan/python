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