# from threading import *
# from time import sleep

# class task1(Thread):
#     def run(self):
#         for i in range(5):
#             print("the task is taken")
#             sleep(1)
    
# class task2(Thread):
#     def run(self):
#         for i in range(5):
#             print("the task is done")
#             sleep(1)

# obj=task1()
# obj1=task2()

# obj.start()
# obj1.start()


from threading import *
from time import sleep
class user(Thread):
    def run(self):
        for i in range(5):
            print("hey google")
            sleep(1)

class chatbot(Thread):
    def run(self):
        for i in range(5):
            print("hello sir")
            sleep(1)

obj=user()
obj1=chatbot()

obj.start()
obj1.start()
