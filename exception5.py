try:
    num=int(input("Enter any Number : "))
    assert num%2==0 

except:
    print("Not an even Number")

else:
    reci=1/num;
    print("reciprocal :",reci)
