import random
while True:
    data=int(input('''
Game Start...
1.Yes
2.No|Exit
'''))
    if data==1:
        Cnumber=random.randrange(1,4)
        Userinput=int(input("Enter Your guess Number : "))
        if Userinput>Cnumber:
            print("Computer Number : ",Cnumber)
            print("Your guess number is too high")

        elif Userinput < Cnumber:
            print("Computer Number : ", Cnumber)
            print("Your guess number is too low")

        else:
            print("Computer Number : ", Cnumber)
            print("Both Numbers are equal")
    else:
        break
