file=open("Employee1.txt","w")
for i in range(3):
    name=input("Enter Name : ")
    id = int(input("Enter Id : "))
    salary = eval(input("Enter salary : "))
    file.write(name+" "+str(id)+" "+str(salary)+"\n")
#file.write(str(id)+" ")
#file.write(str(salary))

file.close()
