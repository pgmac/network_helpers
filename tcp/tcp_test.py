#!/usr/bin/env python

import socket
import argparse

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.settimeout(1)
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Host to test TCP port connection against", default="127.0.0.1")
    parser.add_argument("--port", help="User to connect as", default=22)
    args = parser.parse_args()

    if isOpen(args.host, args.port):
        result = "Success"
    else:
        result = "FAILED"

    print("Connection to {}:{} - {}".format(args.host, args.port, result))
