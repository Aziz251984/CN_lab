from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
msg = input('Input lowercase sentance: ')
clientSocket.send(msg.encode())
returnMsg = clientSocket.recv(1024)
print("Return:", returnMsg.decode(), '\n')
clientSocket.close()

