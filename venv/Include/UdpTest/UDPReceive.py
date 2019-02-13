
import socket

#创建socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',8805))

while True:
    #接收数据:
    data, addr=s.recvfrom(2048)
    print('Received from %s:%s.' % addr)
    print('Receive data is : %s'% data.decode('utf-8'))
