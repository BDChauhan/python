# must - page 148, exercise 37: Symbol review
# https://drive.google.com/file/d/1YHUbG3WGK3R351WX65GcCNPKnB1kB0xe/view

count = [1,2,3,4,5]
fruits = ['apple', 'banana', 'orange', 'watermelon']
mixList = ['yellow', 122, "this is sentence", True]

n = 0
for i in count:
    print(f"element no.{n} of list : {i}", )
    n = n + 1

n = 0
while(n < len(fruits)):
    print(fruits[n])
    n = n + 1
    
# accessing elements of list

print(fruits[-1])
print(fruits[-4])
print(count[3]+10)
count.pop()
print(count)

print(count[1:3]) # it prints only 1st and 2nd element only not 3rd


# Rules for if-statements
# 1. Every if-statement must have an else.
# 2. If this else should never run because it doesn’t make sense, then you
# must use a die function in the else that prints out an error message and
# dies, just like we did in the last exercise. This will find many errors.
# 3. Never nest if-statements more than two deep and always try to do
# them one deep.
# 4. Treat if-statements like paragraphs, where each if-elif-else
# grouping is like a set of sentences. Put blank lines before and after.
# 5. Your Boolean tests should be simple. If they are complex, move their
# calculations to variables earlier in your function and use a good name for
# the variable. 


# break - to exit from loop
# continue - go to beginning of loop
# pass - to execute nothing

# list(mutable) vs tuple(immutable)

