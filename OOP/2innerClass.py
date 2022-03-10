# class inside a class!

from matplotlib.pyplot import cla


class student:
    def __init__(self, name, no):
        self.name = name
        self.no = no
        # self.lap = self.laptop()
        
    def show(self):
        print(self.name, self.no)
        self.lap.show()
        
    class laptop:
        def __init__(self,lapName, ram):
            self.lapName = lapName
            self.ram = ram
        
        def show(self):
            print(self.lapName, self.ram)
            
s1 = student('Brijesh', 11)
s1.lap = student.laptop('Dell',8)
# s1.lap.show()
s1.show()

s2 = student('Brijesh1', 12)

s2.lap = student.laptop('HP', 16)
s2.show()