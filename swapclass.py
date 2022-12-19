class Swap:
      x=int(input("Enter the value of x : "))
      y=int(input("Enter the value of y : "))
      def exchange(self):
            self.x=self.x^self.y
            self.y=self.x^self.y
            self.x=self.x^self.y
      def display(self):
            print("value of x : ", self.x)
            print("value of y : ",self.y)
s=Swap()
s.exchange()
s.display()
