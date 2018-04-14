__author__ = 'song'

###############################################################
#多进程
import os
#linux 下可以使用fork()
#print('Process (%s) start...' % os.getpid())
## Only works on Unix/Linux/Mac:
#pid = os.fork()
#if pid == 0:
#    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
#else:
#    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

#跨平台 multiprocessing

#multiprocessing.Process
from multiprocessing import  Process
import  time

def A():
    print('正在调用函数')
    time.sleep(1)
#windows 运行分布式进程需要先启动 freeze_support()
#...
#需要使用Python常用的 if __name__ == '__main__':来进行是不是主module的判断

if __name__ == '__main__':
    p=Process(target=A)
    p.start()


#Process创建的进程必须执行完，主程序才会结束，用exit()也不能强退
def B(num):
    for i in range(5):
        print('正在调用函数 %d' % num)
        time.sleep(1)
if __name__ == '__main__':
    for i in range(3):
        p=Process(target=B,args=(i,))
        p.start()

#multiprocessing.Process的run()方法
import  os
import time
from multiprocessing import Process

class  NewProcess(Process):  #继承Process类创建一个新类
    def __init__(self,num):
        self.num=num
        super().__init__()
    def run(self):  #重写Process类中的run方法
        for i in range(3):
            print('我是进程%d,我的进程ID是%d'%(self.num,os.getpid()))
            time.sleep(1)
if __name__ == '__main__':
    for i in range(2):
        p=NewProcess(i)
        p.start()

#multiprocessing.Pool 进程池
import time
from  multiprocessing import Pool
def C():
    for i in range(3):
        print(i)
        time.sleep(1)
if __name__=='__main__':
    pool=Pool(2) #定义进程池大小
    for i in range(2):
        pool.apply_async(C)#使用非阻塞方式调用func，阻塞是apply()

    pool.close()    #关闭pool.不再接受其他新的任务
    pool.join()     #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
                    #Pool.terminate()：一旦运行到此步，不管任务是否完成，立即终止


from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('run task %s (%s)...'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('task %s runs %0.2f seconds' % (name,(end-start)))
if __name__=='__main__':
    print('parant process %s' % os.getpid())
    p=Pool(4)
    for i in range(5):
#task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
# 这是因为Pool的默认大小是4，因此，最多同时执行4个进程
#p = Pool(5)，就可以同时跑5个进程。
        p.apply_async(long_time_task,args=(i,))
    print('waiting for all subprocesses done')
    p.close()
    p.join()
    print('all suboprocess done')

###############################################################
#进程间通信
#Queue

from multiprocessing import Process ,Queue
import os,time

#写数据进程
def write(q):
    print('Prrocess  to write  %s'%(os.getpid()))
    for value in (1,2,3):
        print('put %s to queue' % value)
        q.put(value)
        time.sleep(1)

#读数据进程
def read(q):
    print("process to read %s"% os.getpid())
    while True:
        value=q.get(True)
        print('get %s from queue '% value)

if __name__== '__main__':
#父进程创建queue 传给各个子进程
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
#启动子进程 pw，写入
    pw.start()
#启动子进程pr.读取
    pr.start()

#等待读进程结束
    pw.join()
#进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()


###############################################################
#多线程
import  time,threading

#新线程执行的代码
def loop():
    print('thread %s is runing ...'% threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s'% (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
print('thread %s is runing ...'% threading.current_thread().name)
#current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread
t=threading.Thread(target=loop,name='LoopThread')#线程名LoopThread，执行的函数loop
t1=threading.Thread(target=loop,name='LoopThread1')# 线程名LoopThread1
t.start()
t1.start()
t.join()
t1.join()
print('thread %s ended.' % threading.current_thread().name)

###############################################################
#线程锁
balance =0
lock=threading.Lock()

def change_it(n):
    #先存后取
    global balance #函数中使用全局变量，使用global声明
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for i in range(10):
        #获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:  #用try...finally来确保锁一定会被释放
        #释放锁
            lock.release()
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

###############################################################
#ThreadLocal
import  threading
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    std = local_school.studentname
    age = local_school.age
    print('hello ,%s age is %d (in %s )'% (std,age,threading.current_thread().name))
def process_thread(name,age):
    # 绑定ThreadLocal的studentanme and age
    local_school.studentname = name
    local_school.age = age
    process_student()

t1=threading.Thread(target=process_thread,args=('alice',5,),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('bob',6,),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

###############################################################
##分布式进程
#import  random ,time,queue
#from multiprocessing.managers import BaseManager
#
##创建发送任务的队列
#task_queue = queue.Queue()
##创建接收任务的队列
#result_queue = queue.Queue()
#
##从BaseManager继承的QueueManager
#class QueueManeger(BaseManager):
#    pass
##把两个queue都注册到网络上，callable参数关联了queue对象
#QueueManeger.register('get_task_queue',callable=lambda : task_queue)
#QueueManeger.register('get_result_queue',callable=lambda : result_queue)
#
##绑定端口5000，设置验证码'abc'
#manager=QueueManeger(address=('',5000),authkey=b'abc')
#
##启动Queue
#manager.start()
#
##获得通过网络访问的queue对象
#task=manage.get_task_queue()
#result=manage.get_result_queue
#
##放几个任务进去
#for i in range(10):
#    n=random.randint(0,1000)
#    print('put task %d ...' % n)
#    task.put(n)
##从result队列读取结果
#print('get reslut...')
#
#for i in range(10):
#    r=result.get(timeout=10)
#    print('result : %s' %r)
##关闭
#manage.shutdown()
#print()

