from socket import *

serverIP = '127.0.0.1'
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverIP,serverPort))
serverSocket.listen(1)

while(1):
    print("Server Ready!")
    connectionSocket, clientAddr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    file = open(sentence,'r')
    contents = file.read(1024)
    connectionSocket.send(contents.encode())
    file.close()
    serverSocket.close()