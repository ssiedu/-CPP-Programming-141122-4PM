num=int(input("Enter Any Number : "))
if(num%5==0 and num%7==0):
      print("Number is divisible by 5 and 7")
elif(num%7==0):
      print("Number is divisible by 7")
elif(num%5==0):
      print("Number is divisible by 5")
else:
      print("Not divisible by both")

