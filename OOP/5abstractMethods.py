# python by defauld do not support abstract classes 
# but we have module 'abc' = abstract base classes - we can use that to create our own abstract classes
# when method has body --> normal method
# if it is blank/ method is only declared (pass) --> abstract method
# class which have atleast 1 abstract method --> abstract class - you cannot create obj of it
#   you have to import abc and abstractmethod - use decorator for method

# Use of it???
#   when designing application - following oops concepts
#   to make some methods compulsory in some classes - kind of restrictions - lets say for API
#   find more uses

from abc import ABC, abstractmethod

from matplotlib.pyplot import cla

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
    
# class computer is abstract class here --> you cant instantiate abstract class like below
# com = computer()
# com.process()

class laptop(computer):
    def process(self):
        print("Running")
    
lap = laptop()
lap.process()