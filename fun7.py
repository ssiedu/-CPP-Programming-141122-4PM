def info(**kwarg):
    print(kwarg)
    print("name is : ",kwarg['name'])
    print("Age is : ",kwarg['age'])

info(name='ram',age=45,salary=67000)
