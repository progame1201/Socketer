import socket
import os
class Socketer():
   #Socketer
 def __init__(self):
  self.success = True
 def udp(self, ip="1.1.1.1", port="80"): # standard values ip=1.1.1.1 port=80
  try:
   ip = str(ip) #ip
   port= int(port) #port
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket
   sock.settimeout(2) # timout time
   sus = sock.connect((ip, port)) # connecting
   sock.close() # sock closed
  except TimeoutError: # timeout error
   self.success = False # return false
  except ConnectionError: #connection eror
   self.success = False # return false
 def tcp(self, ip="1.1.1.1", port="80"): # standard values ip=1.1.1.1 port=80
  try:
   ip = str(ip) #port
   port= int(port) #ip
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket
   sock.settimeout(2) # timout time
   sus = sock.connect((ip, port)) # connecting
   sock.close() # sock closed
  except TimeoutError: # timeout error
   self.success = False # return false
  except ConnectionError: #connection eror
   self.success = False # return false

#example use
#Sock = Socketer()
#request = Sock.tcp()
#tcpresult = tcp.success