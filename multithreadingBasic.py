"""
multi threading: its a concept in python in which we can process multiple task at a time. it dnt 
provide parallelism concept but when one process will be in idle or wait state then multithreading
execute other process to save time.


library to use:
    time:this library is use to generating delay and finding current time of the system.
    threading: thread are initialized and control using it.

functions to use:
    Thread: initialize thread by selecting it. target(process),args(argument)
    start:it starts the thread
    join: waits the system for thread completition.
    


why we do multithreading

import time
def square(n):
    print("this is the function to find the square")
    for i in n:
        print("square of {0} is:-".format(i),i*i)
        time.sleep(0.5)
def cube(n):
    print("this is the function to find the cube")
    for i in n:
        print("cube of {0} is:-".format(i),i*i*i)
        time.sleep(0.5)
t=time.time()
a=[1,2,3,4,5,6]
square(a)
cube(a)
print("time taken by the system is:-",time.time()-t)
"""

import threading
import time
def square(n):
    print("this is the function to find the square")
    for i in n:
        print("square of {0} is:-".format(i),i*i)
        time.sleep(0.5)
def cube(n):
    print("this is the function to find the cube")
    for i in n:
        print("cube of {0} is:-".format(i),i*i*i)
        time.sleep(0.5)
t=time.time()
a=[1,2,3,4,5,6]
t1=threading.Thread(target=square,args=(a,))
t2=threading.Thread(target=cube,args=(a,))
t1.start()
t2.start()
t1.join()
t2.join()

print("time taken by the system is:-",time.time()-t)
