class Number:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def calculate(self):
        self.add=self.num1+self.num2
    def display(self):
        print("sum is : ", self.add)


n=Number(100,200)
n.calculate()
n.display()
