try:
    x=int(input("Enter a number upto 100:"))
    if x>100:
        raise ValueError(x)

except ValueError:
    print(x,"out of range")

else:
    print(x,"with in range")
