import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.12.76', 8088))
filename = '/home/xxj/.vim/vimrc'
print('I want to get the file %s!' % filename)
s.send(filename.encode('utf-8'))
str1 = s.recv(1024)
str2 = str1.decode('utf-8')
if str2 == 'no':
	print('To get the file %s is failed!' % filename)
else:
	s.send(b'I am ready!')
	temp = filename.split('/')
	myname = 'my_' + temp[len(temp) - 1]
	size = 1024
	with open(myname, 'wb') as f:
		while True:
			data = s.recv(size)
			f.write(data)
			if len(data) < size:
				break
	print('The download file is %s.'% myname)
s.close()
