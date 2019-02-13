from socket import *
host='127.0.0.1'
port=8080
bufsize=1024
addr=(host,port)
tcpSocekt=socket(AF_INET, SOCK_STREAM)
tcpSocekt.settimeout(10)
tcpSocekt.connect(addr)

#tcpSocekt.bind(addr)


while True:
    #data=input('send data is:')
    data='(hello)'
    data=data.encode('utf-8')
    if not data:
        break;
    tcpSocekt.send(data)
    data1=tcpSocekt.recv(bufsize)
    print('receive data is:' + data1.decode('utf-8'))
    if not data1 :
        break;
    if data1.decode('utf-8') == '123':
        break

tcpSocekt.close()