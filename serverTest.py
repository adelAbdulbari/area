import socket
def area(message):
    area_commands = ['circle','sequare','rectangle','triangle']
    parts = message.split(',')
    if not (parts[0] in area_commands): return "invalid command"
    elif (parts[0] in ['circle','sequare']):
        if (len(parts)!=2):return "invalid request"
        elif parts[1].isdigit():return "invalid request"
        if parts[0] == 'circle': return (pow(int(parts[1]),2)* 3.14)
        if parts[0] == 'square': return (pow( int( parts[1] ), 2 ))
    elif (parts[0]in ['rectangle','triangle']):
        if (len(parts)!=3):return "invalid request"
        elif parts[1].isdigit() and parts[2].isdigit():return "invalid request"
        if parts[0] == 'rectangle': return (int(parts[1])* int(parts[2]))
        if parts[0] == 'triangle': return ( int( parts[1] )*int(parts[2]))

serverPort = 17000
BUFFER_SIZE = 1024

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print("The sreve is ready to receve")
while 1:

    message, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
    message = message.decode('utf-8')
    response = str(area(message))
    serverSocket.sendto(response.encode('utf-8'),clientAddress)

    print(str(message)+' = ' + str(response))
serverSocket.close()
