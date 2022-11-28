num1=eval(input("Enter First Number : "))
num2=eval(input("Enter Second Number : "))
print(" 1.(+)Addition\n 2.(-)Subtraction\n 3.(*)Multiplication\n 4.(/)Division")
ch=input("Enter Your choice : ")
match ch:
      case '+':
            print("Addition : ",num1+num2)
      case '-':
            print("Subtraction : ", num1-num2)
      case '*':
            print("Multiplication : ", num1*num2)
      case '/':
            print("Division : ", num1/num2)
      case _:
            print("Please Enter valid choice ")
