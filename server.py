import socket 

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 9500 
address = (ip,port)

server.bind(address)
server.listen(1)
print ("start listening",ip,port)

client,addr = server.accept()
print ("Got a connection from", addr[0], addr[1])

while True: 
    data = client.recv(1024)
    print ("recieved", data)
    if (data == b'Hello'):
        client.send (b'Hi')
        
    else:
        client.send(b'goodbye')
     
