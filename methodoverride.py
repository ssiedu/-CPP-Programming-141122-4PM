class Demo:
    def __init__(self):
        print("This is Base class function ")

class sub(Demo):
    def __init__(self):
        super().__init__()
        print("This is derive class function")


s=sub()
#s.display()

