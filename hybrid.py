class Base:
    def __init__(self):
        self.x=int(input("Enter x : "))
        self.y=int(input("Enter y : "))

class child1(Base):
    def getSum(self):
        self.add=self.x+self.y


class child2:
    def getData(self):
        self.x=int(input("Enter x : "))
        self.y=int(input("Enter y : "))
    def getMul(self):
        self.mul=self.x*self.y

class subchild(child1,child2):
    def display(self):
        print("Sum is : ",self.add)
        print("Mul is : ",self.mul)


c=subchild()
c.getSum()
c.getData()
c.getMul()
c.display()




        
        
