class Number:
    def __init__(self,num1=20,num2=10):
        self.num1=num1
        self.num2=num2
    def __init__(self):
        self.num1=100
        self.num2=200
    def calculate(self):
        self.add=self.num1+self.num2
    def display(self):
        print("sum is : ", self.add)


n=Number()
n.calculate()
n.display()
