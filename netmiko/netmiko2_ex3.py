import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime

password = getpass()

start_time = datetime.now()
device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios"
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

cfgs = ['show version', 'show lldp neighbors']

for cfg in cfgs:
    output = net_connect.send_command(cfg, use_textfsm=True)
    print("#" * 80)
    print(cfg)
    print("#" * 80)
    pprint(output)
    print("#" * 80)
    print()

    if cfg == "show lldp neighbors":
        print("LLDP Data Structure Type: {}".format(type(output)))
        print("HPE Switch Connection Port: {}".format(output[0]["neighbor_interface"]))

print()
net_connect.disconnect()
