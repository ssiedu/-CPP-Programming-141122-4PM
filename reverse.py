num=int(input("Enter any Number : "))
temp = num
rev=0
sum=0
tod=0
while(num!=0):
      rev = rev*10 + num%10
      sum = sum + num%10
      num = num//10
      tod = tod+1

print("Reverse number : ", rev)
print("sum of digit : ", sum)
print("Total no of digit : ", tod)

if(temp==rev):
      print("Number is pallindrome")
else:
      print("Number is not pallindrome")
