#!/usr/bin/python
# -*- coding: UTF-8 -*-
import thread
import time
import threading
"""
# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))


# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 2))
    thread.start_new_thread(print_time, ("Thread-2", 4))
except:
    print "Error: unable to start thread"

while 1:
    pass
"""


exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        print_time2(self.name, self.counter, 3)
        print "Exiting " + self.name



def print_time2(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print "%s: %s \n" % (threadName, time.ctime(time.time()))
        counter -= 1


thread1 = myThread(1, "Thread-1", 3)
thread2 = myThread(2, "Thread-2", 4)

# thread1.start()
# thread2.start()





class syncThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting: " + self.name
        threadLock.acquire()
        print_time2(self.name, self.counter, 3)
        threadLock.release()

threadLock = threading.Lock()
threads = []

thread3 = syncThread(3, "Thread-3", 1)
thread4 = syncThread(4, "THread-4", 2)

thread3.start()
thread4.start()

threads.append(thread3)
threads.append(thread4)


for t in threads:
    t.join()

print "Exiting main Thread"




import Queue
exitFlag1 = 0

class queueThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q;

    def run(self):
        print "Starting  " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name


def process_data(threadName, q):
    while not exitFlag1:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s Process %" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)



queueLock = threading.Lock()
workQueue = Queue.deque()
threadList = ["THread-1", "THread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
threads1 = []
threadID = 1

# 创建新线程

for tName in threadList:
    thread = queueThread(threadID, tName, workQueue)
    thread.start()
    threads1.append()
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()


# 等待队列清空
while not workQueue.empty():
    pass

exitFlag1 = 1

# 等待所有线程完成
for t in threads1:
    t.join()

print "Exiting main thread"
