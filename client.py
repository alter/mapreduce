#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import json

print( 'Client started' )

data = [{ 'type': 'test1', 'value': 'Just a test1' }, { 'type': 'test2', 'value': 'Just a test2' }, { 'type': 'spam', 'value': 'ololo' }, { 'ololo':'123' }]
sock = socket.socket()
sock.connect(('localhost', 30000))
json_data = json.dumps( data )
sock.send( json_data )
sock.close()

