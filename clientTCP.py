from socket import *

serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
sentence = input("File name:")
clientSocket.send(sentence.encode())
filecontents = clientSocket.recv(1024).decode()
print(filecontents)
clientSocket.close()