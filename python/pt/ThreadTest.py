
import threading
import time
import queue

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程:"+self.name)
        print_time(self.name,self.counter,5)
        print("退出线程:"+self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s"%(threadName,time.ctime(time.time())))
        counter-=1

# thread1 = myThread(1,"Thread-1",1)
# thread2 = myThread(2,"Thread-2",2)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print("退出主线程")
threadLock = threading.Lock()
threads = []
class myThread2(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程"+self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()

# thread1 = myThread2(1,"Thread-1",1)
# thread2 = myThread2(2,"Thread-2",2)
#
# thread1.start()
# thread2.start()
#
# threads.append(thread1)
# threads.append(thread2)
#
# for t in threads:
#     t.join()
#
# print("退出主线程")
threadList = ["Thread-1","Thread-2","Thread-3"]
nameList = ["One","Two","Three","Four","Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threadID = 1
class myThread3(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("开启线程:"+self.name)
        process_data(self.name,self.q)
        print("退出线程:"+self.name)

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" %(threadName,data))
        else:
            queueLock.release()
        time.sleep(1)
# 创建新线程
for tName in threadList:
    thread = myThread3(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID+=1

# 填充队列
queueLock.acquire()
for work in nameList:
    workQueue.put(work)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")