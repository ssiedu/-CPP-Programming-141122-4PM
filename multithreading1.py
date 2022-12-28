from threading import Thread
import time
class Welcome(Thread):
    def run(self):
        for i in range(5):
            print("Welcome")
            time.sleep(0.3)


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(0.3)



t1=Welcome()
t2=Hello()
t1.start()
time.sleep(0.3)
t2.start()
t1.join()
t2.join()
print("Bye")
