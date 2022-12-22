from multipledispatch import dispatch

@dispatch(int,int)
def product(first,second):
    result=first*second
    print("result:",result)

@dispatch(int,int,int)
def product(first,second,third):
    result=first*second*third
    print("result : ",result)

@dispatch(float,int)
def product(first,second):
    result=first*second
    print("result:",result)

@dispatch(int,int,float)
def product(first,second,third):
    result=first*second*third
    print("result : ",result)

product(2.1,4)
product(3,4,2.2)
product(1,2)
product(1,2,3)

    
