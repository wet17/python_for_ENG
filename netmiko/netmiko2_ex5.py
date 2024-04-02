import os
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

device1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "fast_cli": True
}
device2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "fast_cli": True
}

for device in (device1, device2):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_config_from_file("my_vlans.txt")
    print(output)
    save_out = net_connect.save_config()
    net_connect.disconnect()
