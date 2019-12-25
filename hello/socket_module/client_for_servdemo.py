__author__ = 'song'
import socket
#配套的client
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect(('127.0.0.1',9999))
s.connect(('192.168.10.76',9999))   
print(s.recv(1024).decode('utf-8'))
for data in [b's',b'o',b'n',b'g',b'z',b'h',b'e',b'exit']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()