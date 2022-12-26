file=open("Employee.txt","w")
name=input("Enter Name : ")
id = int(input("Enter Id : "))
salary = eval(input("Enter salary : "))
file.write(name+" "+str(id)+" "+str(salary))
#file.write(str(id)+" ")
#file.write(str(salary))

file.close()
