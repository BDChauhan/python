class A:
    def __init__(self):
        print("init of A")
        
    def feature1(self):
        print("Feature 1 in class A")
        
    def feature2(self):
        print("Feature 2 in class A")

class B(A): #B in inheriting all feature of A
    def __init__(self):
        super().__init__()
        print("init of B")
    def feature3(self):
        print("Feature 3 in class B")
    
    def feature1(self):
        print("exmple of method overriding - overriding feature 1 of class A")
        
a1 = A()
b1 = B()
a1.feature1()
b1.feature2()
b1.feature1()

# inheritance
# (1)single level, (2)multi level, (3)multiple 

# to inherit more than one class --> class c(A,B)

# constructor in inheritance?
#   if B is extending A and if both have __init__ (constructor) --> it will try to find __init__ of B then it will go in parent
#   with help of super() --> you can call all methods of super class

#   what will happen with super() in case of multiple inheritance???? 
# MRO = 'Method Resolution Order' comes in picture --> it will starts finding __init__ from left to right
#   fr ex, class C(A,B) --> it will find method in C then in A then in B
