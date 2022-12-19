class Area:
      r=eval(input("Enter radius of circle : "))
      def calculate_Area(self):
            self.area=3.14*self.r*self.r
      def display(self):
            print("Area of circle : ",self.area)

a=Area();
a.calculate_Area()
a.display()
      
