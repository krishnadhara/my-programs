from multiprocessing import Process

def call_name(name):
    print('hello',name)    #hello dreamwin

if __name__ =="__main__":
    p=Process(target=call_name,args=("dreamwin",))
    p.start()

########Creating multiple process###############
from multiprocessing import Process ,current_process
def worker(num):
    print("process",num)         # process num 1,name=krishna,pid:3220
    print(current_process().name) # process num 2,name=dhara,pid:11328
    print(current_process().pid)
if __name__ =="__main__":
    p1=Process(name="krishna",target=worker,args=(1,))
    p2=Process(name='dhara',target=worker,args=(2,))

    p1.start()
    p2.start()
#################### Multiprocessing Queue #############
from multiprocessing import process,Queue
import time
import random
def producer(Q):
    while True:
        num=random.randint(1,100)
        time.sleep(1)
        Q.put(num)
def consumer(Q):
    while True:
        time.sleep(1)
        print (Q.get())
if __name__=="__main__":
    Q = Queue(5)
    p1=Process(name="reddy",target=producer,args=(Q,))
    p2= Process(name="laksmi",target=consumer,args=(Q,))
    print("start")
    p1.start()
    p2.start()

