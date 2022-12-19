class Addition:
      def getdata(self):
            self.x=int(input("Enter the value of x : "))
            self.y=int(input("Enter the value of y : "))
      def calculate(self):
            self.add=self.x+self.y
      def display(self):
            print("sum is : ",self.add)

A=Addition()
A.getdata()
A.calculate()
A.display()
B=Addition()
B.getdata()
B.calculate()
B.display()
