class First:
    def __init__(self,num1,num2):
        self.x=num1
        self.y=num2
        #print(num1)
        #print(num2)
        #self.x=int(input("Enter the value of x : "))
        #self.y=int(input("Enter the value of y : "))

class Second(First):
    def calculate(self):
        self.add=self.x+self.y


class Third(Second):
    def display(self):
        print("Sum is : ",self.add)



t=Third(num2=10,num1=20)
t.calculate()
t.display()
#print(num1)
#print(num2)
