import socket
serverIP = '127.0.0.1'
serverPort = 17000
BUFFER_SIZE = 1024
clintSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
    shape = input( "select shape:" )

    if not (shape in ['circle', 'sequare', 'rectangle', 'triangle']):
        print( 'please select valid sharpe!' )
        continue
    elif (shape == 'circle'):
        x = input( "please input redius:" )
        message = 'circle,' + x
    elif (shape == 'square'):
        x = input( "please input side:" )
        message = 'square,' + x
    elif (shape == 'rectangle'):
        x = input( "please input width:" )
        y = input( 'please input height:' )
        message = 'rectangle,' + x + ',' + y
    elif (shape == 'triangle'):
        x = input( "please input base:" )
        y = input( "please input height:" )
        message = 'triangle,' + x + ',' + y
    clintSocket.sendto(message.encode('utf-8'),(serverIP,serverPort))
    response , address = clintSocket.recvfrom(BUFFER_SIZE)
    print (message + ' = ' + response.decode('utf-8'))
clintSocket.close()