import socket
import psutil
def do_cpu():
	data = str(psutil.cpu_percent(0)) + '%\n'
	count = 0
	for process in psutil.process_iter():
		data = data + process.name()
		data = data + ',' + str(process.pid)
		cpu_usage_rate_process = str(process.cpu_percent(0)) + '%'
		data = data + ',' + cpu_usage_rate_process + '\n'
		count += 1
		if count == 10:
			break
		return data
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.12.76', 8090))
print('Bind UDP on 8090')
while True:
	(info,addr) = s.recvfrom(1024)
	data = do_cpu()
	s.snedto(data.encode(utf-8,addr))
	print('The client is ', addr)
	print('Sended CPU data is :', data)
