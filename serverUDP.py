from socket import *

serverIP = '127.0.0.1'
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind((serverIP,serverPort))

while(1):
    print("READY")
    sentence,clientAdd =  serverSocket.recvfrom(2048)
    sentence = sentence.decode()
    file = open(sentence,'r')
    cont = file.read(2048)
    serverSocket.sendto(bytes(cont,'utf-8'),clientAdd)
    file.close()
    serverSocket.close()