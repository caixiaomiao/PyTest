import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    #sock.send(b'Welcome!')
    i=0
    while True:
        data = sock.recv(8192)
        #time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        #sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        i=i+1
        print('receive %s data' %i)
        sock.send('(ok)'.encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',8080))
s.listen(10)
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


