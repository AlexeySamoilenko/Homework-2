from threading import Thread, RLock
import time


a = 0
lock = RLock()

def function(arg):
    global a
    lock.acquire()
    #a += arg <- much faster)
    for _ in range(arg):
        a += 1
    lock.release()

def main():
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(1000000,))
        thread.start()
        threads.append(thread)
        
    [t.join() for t in threads]
    print("----------------------", a)  # ???


main()

''' with args=(10000000,)
    without lock      5.983 seconds
    with lock         6.895 seconds
    with Rlock        6.068 seconds
    without for: a+=1 0.018 seconds'''
