#!/usr/bin/env python2

import socket
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--endpoint", default="10.11.50.5", help="Endpoint host to connect to")
parser.add_argument("-p", "--port", type=int, default=500, help="Endpoint host to connect to")
args = parser.parse_args()
endpoint = args.endpoint
port = args.port

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (endpoint, port)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    print >>sys.stderr, '{}:{} - sending "{}"'.format(endpoint, port, message)
    sent = sock.sendto(message, server_address)
            
    # Receive response
    print >>sys.stderr, '{}:{} - waiting to receive'.format(endpoint, port)
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, '{}:{} - received response "{}"'.format(endpoint, port, data)
    
finally:
    print >>sys.stderr, '{}:{} - closing socket'.format(endpoint, port)
    sock.close()
