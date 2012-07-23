#!/usr/bin/env python

"""
A very simple http server -- first version
"""

HOST = "localhost"
PORT = 55555

import socket
import datetime

#create an INET, STREAMing socket
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#bind the socket to localhost, high port
serversocket.bind(('localhost', 55555),)

#become a server socket
serversocket.listen(1) #only accept on connection

html = open('tiny_html.html').read()

def OK_response(body):
    header = []
    header.append("HTTP/1.0 200 OK")
    
    dt = datetime.datetime.now()
    header.append("Date: %s"%dt.isoformat())
    #header.append("Date: Fri, 31 Dec 1999 23:59:59 GMT")
    header.append("Content-Type: text/html")
    header.append("Content-Length: %i"%len(body))
    header.append("")
    header.append(body)
    
    return '\r\n'.join(header)

# accept a single request
#while True:
if True:
    #accept connections from outside
    print "calling accept"
    (clientsocket, address) = serversocket.accept()
    print "accept returned"
    #now do something with the clientsocket
    #in this case, we'll pretend this is a threaded server
    #ct = client_thread(clientsocket)
    #ct.run()
    print "got something:", clientsocket
    print "from address", address
    clientsocket.recv(1024)
    
    # now lets send something:
    response = OK_response(html)
    print response
    clientsocket.send(response)
    #clientsocket.send(html)


del serversocket 
## put this in your browser while this is running:
##    http://localhost:55555/a_file