__author__ = 'song'

import threading
import socket,time
import operator
import sys
class Client(object):
    def __init__(self,sock,addr,thread):
        self.sock = sock  
        self.addr = addr
        self.thread = thread
        print('new client info')
        print(self.sock,self.addr)

    def print_socket(self):
        print('client info')
        print(self.sock,self.addr)


#保存clien的list
#self.conn_pool
#listen线程的socket
#self.soket_listen
#listen线程
#self.thread_listen

#广播线程的socket
#self.sock_broadcast
#广播线程
#self.thread_broadcast

class client_manage(object):
    def __init__(self):
        #保存连接
        self.conn_pool = []

        #用于监听的
        self.soket_listen=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.soket_listen.bind(('0.0.0.0', 9999))
        self.soket_listen.listen(10)

        #用于广播的
        self.sock_broadcast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock_broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.broadcast_addr = ('192.168.1.255', 7777)

    def broadcast(self):     
        while True:
            time.sleep(1)
            self.sock_broadcast.sendto(b'server_ip',self.broadcast_addr)

    def start_broadcast(self):
        self.thread_broadcast = threading.Thread(target= client_manage.broadcast,args=(self,))
        self.thread_broadcast.start()

    def new_client_process(self,sock,addr):
        print('accept new connection from %s:%s' % addr)
        #Client中有__init__方法，实例时传入的参数得与__init__方法的参数匹配，self不需要传    
        sock.send(b'welcome')
        while True:
            data = sock.recv(1024)
            print('recive data:%s' % data)

            #客户端请求断开
            if not data or data.decode('utf-8') == 'exit':
                for i in range(len(self.conn_pool)):
                    if operator.eq(sock,self.conn_pool[i].sock): 
                        self.conn_pool.remove(self.conn_pool[i])
                print('---------剩余的socket---------')
                for i in range(len(self.conn_pool)):
                    print (self.conn_pool[i].sock)
                print('---------剩余的socket---------')
                sock.close()
                print('close Connection from %s:%s closed.' % addr)
                break
            else:
            #客户端发送过来的消息
                sock.send(('server recive: %s!' % data.decode('utf-8')).encode('utf-8'))


    def  listen(self):
        while True:
            sock,addr=self.soket_listen.accept()
            thread_new_client=threading.Thread(target=client_manage.new_client_process,args=(self,sock,addr))
  
            new_client = Client(sock,addr,thread_new_client)          
            self.conn_pool.append(new_client)
            print('---------已经链接的soket---------')
            for i in range(len(self.conn_pool)):
                print (self.conn_pool[i].sock)
            print('---------已经链接的soket---------')
            thread_new_client.start()

    def start_listen(self):
        print('waiting for connection ...')
        self.thread_listen=threading.Thread(target=client_manage.listen,args=(self,))
        self.thread_listen.start()

manager = client_manage()
manager.start_broadcast()
manager.start_listen()

