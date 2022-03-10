from gevent import config


class computer:
    company = 'Dell'
    
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("config is:", self.cpu, self.ram)
    
    @classmethod #decorator
    def cName(cls):
        print(computer.company)
    
    @staticmethod
    def extraMethod():
        print("static method - nothing to do with class/instance var")
    
com1 = computer('i5',16)
computer.config(com1)
com1.config()

com2 = computer('amd', 8)
com2.config()

# every time you create obj, it is allcated to new space, so this print will give diff values every time
print(id(com1))
print(id(com2))

# com1.country() --> will throw err
computer.cName()
com1.extraMethod()
computer.extraMethod()

# size of an object depends upon
#   - no of variables, size of var
#   - data we pass
# who allocates size to obj?? --> constructor - calls __init__ method implicitly

# types of variables - 
#   - instance var: inside any method/init - use obj name to use (c1.avg)
#   - static/class var: outside method but inside class (ofc!!) - can use obj/class name to use var (c1.wheels or car.wheels)

# types of methods - 
#   1. instance methods: accessor methods = getters, mutators = setters (changes val) - will use 'self' keyword
#   2. class methods: when u want to work with class var - will use 'cls' keyword - you have to define it by decorator
#   3. static methods: someting we need to perform which no concerns class/instance var

    