#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import json
import sqlite3

print('Server started')

con = sqlite3.connect('msg.db')
cur = con.cursor()

cur.execute('create table if not exists messages(value varchar(255))')
con.commit()

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('',40000))
sock.listen(1)

while True:
  conn, addr = sock.accept()

  data = conn.recv(1024)
  cmd = "INSERT INTO messages(value) VALUES('"+data+"')"
  cur.execute(cmd)
  con.commit()
  conn.close() 

sock.close()
con.close()
