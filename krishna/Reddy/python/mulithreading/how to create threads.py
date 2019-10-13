import threading
import os
def print_cube(num):
    cube=num*num*num
    print(cube)
def print_sqr(num):
    sqr=num*num
    print(sqr)
if __name__=="__main__":
    t1=threading.Thread(target=print_cube,args=(10,))
    t2=threading.Thread(target=print_sqr,args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("ok")
#############################################
def task1():
    