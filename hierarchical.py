class Base :
    def __init__(self):
        self.x=int(input("Enter First value : "))
        self.y=int(input("Enter second value :"))


class child1(Base):
    def getSum(self):
        self.add=self.x+self.y
        print("sum of two numbers : ",self.add)

class child2(Base):
    def getMul(self):
        self.mul=self.x*self.y
        print("Mul of two numbers : ",self.mul)

class child3(Base):
    def getsquare(self):
        self.s=self.x*self.x
        print("square of a number is :",self.s)

c1=child1()
c1.getSum()
c2=child2()
c2.getMul()
c3=child3()
c3.getsquare()
