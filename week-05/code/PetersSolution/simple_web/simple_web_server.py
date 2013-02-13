#!/usr/bin/env python

import socket
import subprocess
import threading
import time
import os

# Configuration Options:
HOST = '' # listen on all connections (WiFi, etc) 
PORT = 50000 
BACKLOG = 5 # how many connections can we stack up
THREAD_MAX = 5 # How many connections do we handle
BLOCK_SIZE = 1024 # number of bytes to receive at once
# All uris are resolved from the web subdirectory of the current working directory.
LOCAL_WEB = os.path.join( os.getcwd(), "web" )

# Supported request types.
GET = 'get'

def parse_request( header ):
    # GET /favicon.ico HTTP/1.1
    # Host: localhost:50000
    # Connection: keep-alive
    # Accept: */*
    # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11
    # Accept-Encoding: gzip,deflate,sdch
    # Accept-Language: en-US,en;q=0.8
    # Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3
    chunks = header.split( "\r\n" )
    tmp_resource = ''
    type = ''
    if "GET" in chunks[0]:
        type = GET
        c_parts = chunks[0].split( " " )
        tmp_resource = c_parts[1]
        protocol = c_parts[2]
    return ( type, tmp_resource, protocol )

def make_header( response_code, msg='OK', content_length=0, content_type='text/html' ):
    # HTTP/1.1 200 OK
    # Fri, 27 Jul 2012 06:06:28 GMT
    # Content-Type: text/html
    # Content-Length: 170
    header = []
    header.append( "HTTP/1.1 %d %s" % ( response_code, msg ) )
    # Date Format: Fri, 31 Dec 1999 23:59:59 GMT
    header.append( time.strftime( "%a, %d %b %Y %H:%M:%S GMT", time.gmtime( time.time() ) ) )
    header.append( "%s: %s" % ( "Content-Type", content_type ) )
    header.append( "%s: %s" % ( "Content-Length", content_length ) )
    header.append( "" )
    header.append( "" )
    return "\r\n".join( header )

def make_response( uri ):
    # content request type handlers. Note that more than one extension may map to a 
    # single handler to take care of platform differences such as 'html' vs 'htm'
    handlers = {}
    handlers['txt'] = show_text
    handlers['html'] = show_web
    handlers['htm'] = show_web
    handlers['jpeg'] = show_img
    handlers['jpg'] = show_img
    handlers['png'] = show_img
    handlers['gif'] = show_img
    handlers['py'] = do_py
    # Trim off the leading / from the uri or else os.path.join gets cranky...
    args = []
    if ( '?' in uri ):
        uri, arg_str = uri.split( '?' )
        args = arg_str.split( '&' )
    response = ""
    path = os.path.join( LOCAL_WEB, uri[1:] )
    if ( os.path.exists( path ) ):
        # do_handle_request will catch any exception and return a 500. The caller 
        # doesn't need to know the issue, it could even be a security hole.... 
        # so no try excepts in these handlers... Let it fall through.
        if ( os.path.isdir( path ) ):
            return list_dir( uri, path )
        elif ( os.path.isfile( path ) ):
            ext = path.split( '.' )[-1]
            if ( ext == 'py' ):
                return do_py( path, *args )
            elif ( ext in handlers ):
                return handlers[ext]( path )
    return ( None, None )

def list_dir( uri, path ):
    # Get the directory content and build a web display of the data.
    # if the directory is not the document root, make a .. entry for one up...
    dir_list = os.listdir( path )
    out = []
    out.append( '<html><head><title>Files at %s</title></head>' % ( uri ) )
    out.append( '<body><h1>Listing of %s</h1><ul>' % ( uri ) )
    uri_parts = os.path.split( uri )
    if ( uri_parts[1] != '' ):
        out.append( '<li><a href="%s">..</a></li>' % ( uri_parts[0] ) )
    for item in dir_list:
        out.append( '<li><a href="%s">%s</a></li>' % ( os.path.join( uri, item ), item ) )
    out.append( '</ul></body></html>' )
    response = "".join( out )
    return ( 'text/html', response )
    
def show_text( path ):
    fh = open( path )
    txt = fh.read()
    fh.close()
    return ( 'text/plain', txt )

def show_web( path ):
    fh = open( path )
    web_page = fh.read()
    fh.close()
    return ( 'text/html', web_page )

def show_img( path ):
    mime_types = { 'png' : 'png', 'jpeg' : 'jpeg', 'jpg' : 'jpeg', 'gif' : 'gif' }
    ext = path.split( '.' )[-1]
    fh = open( path, 'rb' )
    img_data = fh.read()
    fh.close()
    return ( 'image/%s' % mime_types[ext], img_data )

def do_py( path, *args ):
    # This is horrible security and would be a massive hole should this be used for the
    # real world.... but for demo purposes...
    cli = [ 'python', path ]
    cli.extend( args )
    p = subprocess.Popen( " ".join( cli ), shell=True, stdout=subprocess.PIPE )
    output = p.stdout.read()
    p.stdout.close()
    return ( 'text/html', output )

def do_handle_request( ( client ) ):
    # Get Client Data: Only accepting GET headers for now...
    # If we start doing post. this wont work... Need to loop till we get all the data.
    data = client.recv( BLOCK_SIZE )
    if data: # if the connection was closed there would be no data
        # response header and data as appropriate
        parts = []
        try:
            type, uri, protocol = parse_request( data )
            if ( type == GET ):
                type, response = make_response( uri )
                if response:
                    parts.append( make_header( 200, 'OK', len( response ), type ) )
                    parts.append( response )
                else:
                    parts.append( make_header( 404, 'Not Found' ) )
            else:
                data = 'Simple server only handles GET requests currently...'
                parts.append( make_header( 500, 'Error' ) )
                parts.append( data )
        except Exception, e:
            print "Ouch: %s" % ( e )
            parts.append( make_header( 500, 'Error' ) )
        client.send( "".join( parts ) ) 
        client.close()

def clean_up( pool ):
    keys = pool.keys()
    for name in keys:
        if not pool[name].is_alive():
            del pool[name]
            
if __name__ == "__main__":
    ## create the socket and set options:
    #   AF_INET      - IPV4
    #   SOCK_STREAM  - TCP
    #   SOL_SOCKET   - Key for sockopt but no one knows what its for...
    #   SO_REUSEADDR - Allow Reuse
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ## Bind and start listening.
    s.bind( ( HOST, PORT ) ) 
    s.listen( BACKLOG )
    t_pool = {} # pool of threads.
    i = 0
    while True: # keep looking for new connections forever
        # On connection, get info and 
        # spawn a do_handle_request process...
        client, addr = s.accept()
        if ( len( t_pool ) < THREAD_MAX ):
            name = 'thread%d' % i
            t_pool[name] = threading.Thread( None, do_handle_request, name, ( client, ) )
            t_pool[name].start()
            i += 1
        clean_up( t_pool )
        
            
