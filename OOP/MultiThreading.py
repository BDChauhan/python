# Thread - lightweight process ( one task --> mul process --> one process --> mul thread)
# why we need thread - multitasking

# by default - every execution has one thread = main thread

# class has to be subclass of Thread to use thread & method name inside it should be 'run()'
# can we use other method than run?

from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self) -> None:
        for i in range(5):
            print("Hello")
            # sleep(1) use sleep if it isnt printing simultaneously 

class Hi(Thread):
    def run(self) -> None:
        for i in range(5):
            print("Hi")
            # sleep(1)
            
t1 = Hello()
t2 = Hi()

t1.start() # we arent using run() to call run method, use start() --> It must be called at most once per thread object. It arranges for the object's run() method to be invoked in a separate thread of control.
t2.start()


