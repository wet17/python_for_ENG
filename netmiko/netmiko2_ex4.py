import os
from getpass import getpass
from netmiko import ConnectHandler
from pprint import pprint

password = getpass()

device1 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "fast_cli": True
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

cfgs = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup'
]

output = net_connect.send_config_set(cfgs)

print()
print("#" * 80)
print("CFG Change: ")
print(output)
print("#" * 80)
print()

ping_output = net_connect.send_command("ping www.google.ch")
if "!!" in ping_output:
    print("Ping successfull")
    print("\n\nPing Output: {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing Failed: {}\n\n".format(ping_output))

net_connect.disconnect()

