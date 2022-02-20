# fibonacci series n1,n2,n3,...
# n3 = n2+n1
# 

def fib(n):
    n0 = 0
    n1 = 1
    if n==1:
        print(n0)
    if n<=0:
        print("please enter positive value")
    else:
        print(n0)
        print(n1)
        for i in range(2,n):
            c = n0+n1
            n0 = n1
            n1 = c
            print(c)
    
fib(3)

# try last num that is <100
