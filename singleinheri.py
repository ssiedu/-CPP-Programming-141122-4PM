class First:#base
    def getdata(self):
        self._num1=int(input("Enter First number : "))
        self._num2=int(input("Enter Second Number : "))


class Second(First):#derive class
    def calculate(self):
        self.__add=self._num1+self._num2
        print("Sum is : ", self.__add)


s=Second()
s.getdata()
s.calculate()
print(s._num1)
print(s._num2)
