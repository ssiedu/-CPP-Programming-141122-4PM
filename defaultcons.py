class Addition:
    x=int(input("Enter First number : "))
    y=int(input("Enter Second Number : "))
    def calculate(self):
        self.add=self.x+self.y
    def display(self):
        print("Hello")
        print("Addition is : ",self.add)

a=Addition()
a.calculate()
a.display()
