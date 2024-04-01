import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**cisco3)
print(net_connect.find_prompt())

output = net_connect.send_command("ping", expect_string=r'Protocol', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Target IP', strip_prompt=False, strip_command=False)
output += net_connect.send_command("8.8.8.8", expect_string=r'Repeat', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Datagram', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Timeout', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Extended', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Sweep' ,strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'#', strip_prompt=False, strip_command=False)


net_connect.disconnect()

print()
print(output)
print()
