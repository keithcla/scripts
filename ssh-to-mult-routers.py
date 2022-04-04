# ssh to multiple routers from a file
from netmiko import ConnectHandler
creds = open(r"C:\Users\user\Music\crednotepad.txt")
new_creds = creds.read().splitlines()
user123 = new_creds[0]
pass123 = new_creds[1]
with open(r"C:\Users\user\Music\multidevi.txt") as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'port': 22,
            'username': user123,
            'password': pass123
        }
        net_connect = ConnectHandler(**Router)
        print('Connecting to ' + IP)
        print('-'*79)
        output = net_connect.send_command('sh ip inter brief')
        print(output)
        print()
        print('-'*79)
# Finally close the connection
net_connect.disconnect()