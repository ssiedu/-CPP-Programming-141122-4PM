import pickle
class Student:
    def __init__(self,rno=0,name=" "):
        self.rno=rno
        self.name=name
        self.s1,self.s2,self.s3=0.0,0.0,0.0
    def readMarks(self):
        print("Enter Marks of student : ")
        self.s1=eval(input("Subject 1 : "))
        self.s2=eval(input("Subject 2 : "))
        self.s3=eval(input("Subject 3 :"))
    def display(self):
        print("Roll No : ", self.rno)
        print("Name    : ", self.name)
        print("Subject 1 :", self.s1)
        print("Subject 2 : ", self.s2)
        print("Subject 3 : ", self.s3)

S1=Student(101,"Ram")
S2=Student(102,"Shyam")
S1.readMarks()
S2.readMarks()
file=open("StudentRecord","wb")
pickle.dump(S1,file)
pickle.dump(S2,file)
file.close()
file=open("StudentRecord","rb")
try:
    while True:
        data=pickle.load(file)
        data.display()
except:
    file.close()





