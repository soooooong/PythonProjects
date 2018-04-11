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
    pool.join()     #主进程阻塞，等待子进程的退出，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
                    #Pool.terminate()：一旦运行到此步，不管任务是否完成，立即终止