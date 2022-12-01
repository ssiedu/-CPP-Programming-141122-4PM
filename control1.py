for i in range(1,11):
      if(i>5 and i<8):
            break;
      print(i,end=" ")#1 2 3 4 5
print()
print("===============================")

for i in range(1,11):
      if(i>5 and i<8):
            continue;
      print(i,end=" ")#1 2 3 4 5 8 9 10
print()
print("==============================")
for i in range(1,11,2):
      if(i>5 and i<8):
            pass
      print(i,end=" ")
print()
