#!/usr/bin/env python

"""
A very simple http server -- first version
"""

HOST = "localhost"
PORT = 55555

import socket
import httpdate

#create an INET, STREAMing socket
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#bind the socket to localhost, high port
serversocket.bind(('localhost', 55555),)

#become a server socket
serversocket.listen(1) #only accept one connection

html = open('tiny_html.html').read()

def OK_response(body):
    header = []
    header.append("HTTP/1.0 200 OK")
    
    header.append(httpdate.httpdate_now())
    #header.append("Date: Fri, 31 Dec 1999 23:59:59 GMT")
    header.append("Content-Type: text/html")
    if not body: # for a HEAD request
        header.append("Content-Length: %i"%len(body))
        header.append("")
        header.append(body)
    
    return '\r\n'.join(header)

def fail_404_Response():
    header = []
    header.append("HTTP/1.0 404")
    header.append(httpdate.httpdate_now())
    

def parse_request(request):
    '''
    parse out the request header.
    (only the bits we need)    
    Example request:
    
    GET /a_file HTTP/1.1
    Host: localhost:55555
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:12.0) Gecko/20100101 Firefox/12.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Cache-Control: max-age=0
    '''
    lines = request.split("\r\n")
    print lines
    # the first line should be the request type:
    method, uri = lines[0].split()[:2]
    return (method, uri)


# accept a single request
#while True:
if True:
    #accept connections from outside
    print "calling accept"
    (clientsocket, address) = serversocket.accept()
    print "accept returned"

    #now do something with the clientsocket
    print "got something:", clientsocket
    print "from address", address
    request = clientsocket.recv(1024)
    
    (method, uri) = parse_request(request)
    if method == "HEAD":
        response = OK_response("")
    elif method == "GET":
        response = OK_response(html)
    
    # return the response
    clientsocket.send(response)

del serversocket 

## put this in your browser while this is running:
##    http://localhost:55555/a_file