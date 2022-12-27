import pickle
file=open("list1.dat","wb")
x=[11,22,33,44,55]
pickle.dump(x,file)
file.close()
with open("list1.dat","rb")as file:
    data=pickle.load(file)
    print(data)
file.close()
