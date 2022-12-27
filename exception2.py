try:
    print("try block")
    x=int(input("Enter First Value : "))
    y=int(input("Enter Second value :"))
    z=x/y

except:
    print("Except Block")
    print("Error Occur")

else:
    print("Else Block")
    print("value of z :",z)

finally:
    print("Finally Block")
