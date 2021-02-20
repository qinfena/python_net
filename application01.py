from urllib import request
url = "http://www.baidu.com"
header = {'Accept':'text/html','Connection':'keep-alive'}
req = request.Request(url,headers = header)
response = request.urlopen(req)
print('Status code = ', response.getcode())
print('url = ', response.geturl())
print('info = ', response.info())
