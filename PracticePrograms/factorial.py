# factorial 
#  5! = 5*4*3*2*1

def fact(n):
    if n==0:
        return 1
    if n<0:
        print("Enter positive value")
    else:
        return n * fact(n-1)

x = fact(6)
print(x)