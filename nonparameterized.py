class Number:
    def __init__(self):
        self.num1=int(input("Enter First number : "))
        self.num2=int(input("Enter Second Number : "))
    def calculate(self):
        self.add=self.num1+self.num2
    def display(self):
        print("sum is : ", self.add)


n=Number()
n.calculate(2,3)
n.display()
