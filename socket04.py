import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)
ip = '192.168.12.76'
for port in range(5000,9000):
	result = s.connect_ex((ip,port))
	if result == 0:
		print('port %d is openned!' % port)
s.close()

