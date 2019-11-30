## Today we are going to learn about multi threading

'''
Multithreading is a technique by which we can run multiple programs at one's

Multiple users are start accessing same model or software which is directly connected
to a centralized system.

Thread is a small program which can run which small resource requirement.
Program is a set of instructions.

Program will take all the resources allocated to the software.

To implement multithreading we are importing a library named "threading".
'''

import threading
import os
## To create a thread we have a class named "Thread"

##def add(a):
##
##    ## a will be a list
##
##    sumVal = 0
##    for i in a:
##        sumVal += i
##    print ('Thread name: ' + threading.currentThread().name)
##    print ('Thread pid: ' + str(os.getppid()) + '\n')
##    print ('Thread id: ' + str(threading.currentThread().is_alive()) + '\n')
##    print (f'Sum of the values {max(a)} - {min(a)} is {sumVal}\n')
##
##
##t1 = threading.Thread(target = add, args = ([range(10, 20)]), name = 'thread_10_20')
##t2 = threading.Thread(target = add, args = ([range(1, 200)]), name = 'thread_1_200')
##
##t1.start()
##t2.start()

##from time import sleep
##
##def print_num(a, b):
##
##    for i in range(a, b):
##        print (threading.current_thread().getName(), '\n')
##        print (i, '  ')
##        sleep(2)
##
##t1 = threading.Thread(target = print_num, args = (10, 20), name = 'thread_1')
##t2 = threading.Thread(target = print_num, args = (100, 200), name  = 'thread_2')
##
##t1.start()
##t2.start()



## Join function

###################################################
## Join function is used to make progress simuntaneously.
'''
Thread 1 and thread 2
To wait for another thread to finish and then we will start next thread process. 
'''
###################################################


##def print_sqr(a, b):
##
##    for i in range (a, b):
##        print ('Thread id: ', threading.current_thread().name + '\n')
##        print (str(i ** 2) + '\n')
##
##t1 = threading.Thread(target = print_sqr, args = (10, 20), name = 'thread 1')
##t2 = threading.Thread(target = print_sqr, args = (30, 400), name = 'thread 2')
##t1.start()
##t2.start()
##t1.join()
##t2.join()


