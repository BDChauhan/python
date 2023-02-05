print("this is first line of code")
print("second line!!")
#doing some math
print("python followa PEMDAS or we can say PE(M&D)(A&S)")
print("lets take tqo values a = 10 and b = 4")
a=10
b=4
print("a + b =",a+b, "\na - b =",a-b, "\na * b =",a*b,"\na / b =",a/b,"\na % b =",a%b)

#variables
name = 'Brijesh'
print("My name is {name}")
print(f"My name is {name}")
print("I am a {}".format('student'))

formatter = "{} {}"
print(formatter.format(1,2,3,4))
formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))

print("""another style
      maybe""")

#user input
print("What is your name?")
name = input()
print("your name is", name)

#prompting
age = input("How old are you? ")
print(f"your age: {age}")

# use of argv
from sys import argv

arg1, a2 = argv, argv

print("this is arg1", arg1)
print("second arg:", a2)
