import netifaces
info = netifaces.gateways()
print('info = ', info)
print('type(info) = ', type(info))
gateways_addr = info['default'][2][0]
print('gatway_addr = ', gateways_addr)
