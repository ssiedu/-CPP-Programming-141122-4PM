class Product:
      def getdata(self,a,b):
            self.num1=a
            self.num2=b
      def calculate(self):
            self.result = self.num1 * self.num2
      def display(self):
            print("num1 is : ",self.num1)
            print("num2 is : ",self.num2)
            print("product of two numbers : ",self.result)


p=Product()
x=int(input("Enter First value : "))
y=int(input("Enter Seconmd Number : "))
p.getdata(b=x,a=y)
p.calculate()
p.display()
