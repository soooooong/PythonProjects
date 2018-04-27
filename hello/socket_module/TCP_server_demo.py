__author__ = 'song'
import  threading
import  socket,time
#一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket

#服务器还需要同时响应多个客户端的请求，
#所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了


#创建一个基于IPv4和TCP协议的Socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#监听端口
#用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址
#小于1024的端口号必须要有管理员权限才能绑定,大于的可以自己使用
s.bind(('127.0.0.1', 9999))
s.listen(5)#传入的参数指定等待连接的最大数量
print('waiting for connection ...')

#连接建立后，服务器首先发一条欢迎消息，
# 然后等待客户端数据，并加上Hello再发送给客户端。
# 如果客户端发送了exit字符串，就直接关闭连接
def tcplink(sock,addr):
    print('accept new connection from %s:%s' % addr)
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        print(data)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    print('close')
    sock.close()
    print('Connection from %s:%s closed.' % addr)


#务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
while True:
    #接受一个新链接
    sock,addr=s.accept()
    print(sock,addr)
    print('accepted...')
    #创建新线程处理TCP链接
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()



###############################################################
