__author__ = 'song'
import  threading
import  socket,time

def udpListen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('',7777))

    while True:
        data, addr = sock.recvfrom(100)
        if data == b'server_ip':
            print(addr)
            sock.close()
        break
    
    print('receive server ip addr:', addr, type(addr))



    server_addr = addr[0]
    port = addr[1]
    connct_add = (server_addr,9999)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(connct_add) 

    for data in [b'connct_add1',b'connct_add2',b'connct_add3',b'connct_add4',b'connct_add5',b'exit']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()
    

threading.Thread(target=udpListen).start()
