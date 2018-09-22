import socket                

client = socket.socket()
client.connect(('169.254.41.80' ,9500)) ## this is the address from server when returns "started listening" from server.py


def communicate(data):
    client.send(data)
    print (client.recv(1024))
    return

#Satisfies the requirement when the client "Hello". Should return a hi
communicate(b'Hello')


#Satisfies the requirement when the client any other word. Should return a goodbye
communicate(b'Otherwords')

