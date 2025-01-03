from socket import *

serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
sentence = input("File name")
clientSocket.sendto(bytes(sentence,'utf-8'),(serverIP,serverPort))
contents,serverAddress = clientSocket.recvfrom(2048)
print(contents.decode())
clientSocket.close()