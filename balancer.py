#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import json

print('Balancer started')

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('',30000))
sock.listen(100)

def send_to_server(ip, port, data):
  try:
    sock = socket.socket()
    sock.connect((ip, port))
    sock.send( data )
    sock.close()
  except socket.error as err:
    print "Can't connect to server, error %s" %(err)

while True:
  conn, addr = sock.accept()

  json_str = conn.recv(1024)
  print json_str
  data = json.loads(json_str)
  for i in data:
    if 'type' in i:
      if( i['type'] == 'test1' ):
        print 'send to ip1 ', i['value']
        send_to_server('127.0.0.1', 40000, i['value'])        
      elif( i['type'] == 'test2' ):
        print 'should be send to ip2 ', i['value']
      else:
        conn.close()
      if not data:
        conn.close() 

sock.close()
