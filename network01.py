import psutil
info = psutil.net_if_addrs()
print('info = ', info)
net1 = info['ens33']
net2 = info['lo']
print('net1 = ', net1)
print('net2= ', net2)
print('net1[0] = ', net1[0])
print('net1[1] = ', net1[1])
print('IPv4_addr = ', net1[0].address)
print('IPv6_addr = ', net1[1].address)
