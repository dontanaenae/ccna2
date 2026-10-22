import netmiko
from netmiko import ConnectHandler
import json
import pprint as print

### READ JSON ###
with open('ph.json', 'r') as jfile:
    pfile = json.load(jfile)
    print.pp(pfile)

### Device Information ###
jp = {
    'device_type' : 'cisco_ios',
    'host'        : '192.168.102.12',
    'username'    : 'admin',
    'password'    : 'pass',
    'port'        : 22,
    'secret'      : 'pass'
}


### COMMANDS (should be brackets, not curly braces) ###
config = [
    f'interface {pfile["type"]}{pfile["id"]} 10',
    f'ip add {pfile["ipv4"]["ip"]} {pfile["ipv4"]["mask"]}',
    f'description {pfile["desc"]}',
    'end'
]

### ACCESS ###
cli = ConnectHandler(**jp)
cli.enable()
cli.send_config_set(config)
siib = cli.send_command('show ip int br')
cli.disconnect()


### OUTPUT ### 
print.pp(siib)
