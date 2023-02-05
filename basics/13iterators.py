# iterator - 
# loops vs iterators


nums = [7,8,9,5]

it = iter(nums) #converting list into iterator

print(it) #prints object
print(it.__next__()) #7
print(it.__next__()) #8

print(next(it)) #alternative way to use

# create own iterator - need to create one class with two functions - next and iter

class TopTen:
    def __init__(self) -> None:
        self.num = 1
    
    def __iter__(self):
        return(self)
    
    def __next__(self):
        if self.num <= 2:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
    
vals = TopTen()

print(vals.__next__())
print(next(vals))
print(next(vals))
print("loop")
for i in vals:
    print(i)

