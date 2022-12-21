class First:
    def get_x(self):
        self.x=int(input("Enter First Number : "))


class Second:
    def get_y(self):
        self.y=int(input("Enter Second Number : "))


class Child(First,Second):
    def display(self):
        self.add=self.x+self.y
        print("Sum is : ",self.add)


c=Child()
c.get_x()
c.get_y()
c.display()
