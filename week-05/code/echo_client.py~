import socket 

host = 'localhost' 
port = 50000 
size = 1024 
while True:
    s = socket.socket(socket.AF_INET, 
                      socket.SOCK_STREAM) 
    s.connect((host,port)) 
    msg = raw_input('what should I send? >> ')
    if msg:
        s.send(msg) 
        data = s.recv(size) 
        s.close() 
        print 'Received:', data
    else:
        print "What is the sound of one hand clapping?"
