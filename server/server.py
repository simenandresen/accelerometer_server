#/usr/bin/python
##server.py
import socket
from time import *
import sys 


serv=socket.socket()

HOST=''
#HOST="78.91.80.123"
PORT = 15000   #arbitrary port not currently in use
#ADDR = (HOST,PORT)    #we need a tuple for the address
BUFSIZE = 4096    #reasonably sized buffer for data
 

##bind our socket to the address
try:
	serv.bind((HOST, PORT))    
	serv.listen(5)   
	conn,addr = serv.accept()
except KeyboardInterrupt:
	print "Keyboard Interrupt"
	serv.close()
	exit(1)
try:
	for i in range(0,3100):
		data=conn.recv(4096)
		sys.stdout.flush()
		chunk=data.split()
		sys.stdout.write("0:%s\n" % chunk[-1]) # writes the last element in the list
		sleep(0.03)

	conn.close()
	sleep(10)

except KeyboardInterrupt:
	conn.close()
	print "bye!"
except IndexError:
	conn.close()
	print "indexError"
