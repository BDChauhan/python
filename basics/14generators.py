# generator will give you iterator!
# without defining next/iter function

# why generator - if you are fetching 1000 record and want to print - it will loaded in memory - to deal with one by one value without wasting memory...use generator!


def demo():
    yield 1
    yield 2
    yield 3
    
val1 = demo()
print(next(val1))
print(next(val1))

def sqtopten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1
        
val1 = sqtopten()
l = list(val1)
print(l)
# print(next(val1))
# for i in val1:
#     print(i)