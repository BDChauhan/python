# __name__

# we know that main is starting point of execution.
# same for python - first module is always __main__
# 

from tkinter import Button
import modulee

print ("12specialVar" , __name__) #if u run this file first then it will return __main__

# But if you import modulee (which contains same print) here then it will return something else!
# it will print name of the module

# moment you import library/module, it will execute all code in it
