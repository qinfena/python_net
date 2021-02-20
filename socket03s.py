import socket
import os
def sendfile(conn):
	str1 = conn.recv(1024)
	filename = str1.decode('utf-8')
	print('The client requests my file:', filename)
	if os.path.exists(filename):
		print('I have %s, begin to download!' % filename)
		conn.send(b'yes')
		conn.recv(1024)
		size = 1024
		with open(filename, 'rb') as f:
			while True:
				data = f.read(size)
				conn.send(data)
				if len(data) < size:
					break
		print('%s is download successfully!' % filename)
	else:
		print('Sorry, I have no %s!' % filename)
		conn.send(b'no')
	conn.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.12.76', 8088))
s.listen()
print('Wait for connecting...')
while True:
	(conn,addr) = s.accept()
	sendfile(conn)
