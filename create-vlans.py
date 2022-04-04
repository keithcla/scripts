from netmiko import ConnectHandler
creds = open(r"C:\Users\user\Music\crednotepad.txt")
new_creds = creds.read().splitlines()
devices = open(r"C:\Users\user\Music\switches.txt")
new_devices = devices.read().splitlines()
#configure devices in the file switches.txt
for switches in new_devices:
    dict123 = {
        "device_type": "cisco_ios",
        "username": new_creds[0],
        "password": new_creds[1],
        "ip": switches,
    }
    net_connect = ConnectHandler(**dict123)
    #creating vlans in range xx on switches
    for n in range(2,21):
        print("creating vlan " + str(n))
        config_commands = net_connect.send_config_set((["vlan " + str(n), "name vlan " + str(n)]))
        print(config_commands)
        config_trunk = net_connect.send_config_set((["inter po10", "switchport trunk allow vlan add " +str(n)]))
        print(config_trunk)
    #output the show vlan and sh inter trunk to verify the config
    output_vlan = ("*************************show vlan brief**************************")
    print(output_vlan)
    config_vlan = net_connect.send_command("show vlan brief")
    print(config_vlan)
    output_trunk = ("*************************show inter trunk*************************")
    print(output_trunk)
    config_trunk = net_connect.send_command("show inter trunk")
    print(config_trunk)




