import socket                

client = socket.socket()
ip = socket.gethostbyname(socket.gethostname())
port = 9500 
address = (ip,port)

client.connect(address)


def communicate(data):
    client.send(data)
    print (client.recv(1024))
    return

#Satisfies the requirement when the client "Hello". Should return a hi
communicate(b'Hello')


#Satisfies the requirement when the client any other word. Should return a goodbye
communicate(b'Otherwords')

