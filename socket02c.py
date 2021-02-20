import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.12.76', 8088))
print('I am connecting the server!')
for xx in ['aBch', 'f服务d', 'h7Tq', '.']:
	s.send(xx.encode('utf-8'))
	str1 = s.recv(1024)
	str2 = str(str1,encoding= 'utf-8')
	print('The original string is:', xx,'\t processed string is :', str2)
s.close()
