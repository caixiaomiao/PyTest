import socket

#创建socket连接,socket.SOCK_DGRAM代表udp
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


for data in [b'a',b'b',b'c']:
    s.sendto(data , ('127.0.0.1',8805))

s.close()

