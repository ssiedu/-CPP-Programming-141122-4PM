file=open("Student.txt","a")
for i in range(5):
    name=input("Enter name of student : ")
    file.write(name+"\n")
file.close()
