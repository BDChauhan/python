# polymorphism - many forms/behaviours
#   usage ? - loose coupling, dependency injection, interface
#  4 ways -duck typing, op overloading, method overloading, method overriding

# Duck Typing (similar to interface in Java - explore it)
#   in python it is dynamic typing - 
#   concept arrived from - if a bird walks, swims, quacks like a duck then it is duck
#   similarlly if an object has same methods...it is of no concern from which class it is

class PyCharm:
    def execute(self):
        print("compiling")
    
class myEditor:
    def execute(self):
        print("Running")
        
class laptop:
    def program(self,ide):
        ide.execute() 
        
lap1 = laptop()

ide1 = PyCharm() 
lap1.program(ide1) #it doesn't matter which class of ide is...it should have execute method - duck typing

ide1 = myEditor() #it would also work
lap1.program(ide1)

# type 2 - operator overloading

# overloading = same method name but num of args/type of args are different

#   for + , if we write 2+3 it will call __add__ method of int - if we write a+b it will call __add__ of str
#   in same way, we can create our own __add__ in any class to overload this operator
#   similarly, you can overload any op like >, = etc

class student:
    def __init__(self,m1) -> None:
        self.m1 = m1
     
    def __add__(self,other):
        m1 = self.m1 + other.m1
        s3 = student(m1)
        
        return s3

student1 = student(50)
student2 = student(40)

student3 = student1 + student2
print(student3.m1)

# type 3 - method overloading - in python there is no concept like this 
#   we cannot create two methods with same name

# type 4 - method overriding - in different class, we can create method wth same name and args

#   for example - see 3Inheritance.py
