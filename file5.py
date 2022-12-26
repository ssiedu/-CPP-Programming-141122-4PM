file=open("list2.txt","w")
list1=[]
for i in range(5):
    data=int(input("Enter Elements : "))
    list1.append(str(data)+"\n")
    
file.writelines(list1)
file.close()
