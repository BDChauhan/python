# anoynymous fun = lambda fun/exp
#  f = lambda a : a*a
#  result = f(5)
# define function when u want to use it directly

from functools import reduce


f = lambda a : (a+1) * 100
print(f(2))

nums = [2,5,8,6,5,4,7,8]
# use of lambda
evens = list(filter(lambda n : n%2==0, nums)) 
print(evens)

print(list(map(lambda a : a+2,evens)))

sum = reduce(lambda a,b : a+b, evens)
print("sum of evens", sum)