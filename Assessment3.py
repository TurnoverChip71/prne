#Netmiko library import
from netmiko import ConnectHandler


#Host one input
host = input("Please enter host one ip address:")
username = input("Please enter host one username:")
password = input("Please enter host one password:")
secret = input("Please enter host one secret password:")

#Host two input
host2 = input("Please enter host two ip address:")
username2 = input("Please enter host two username:")
password2 = input("Please enter host two password:")
secret2 = input("Please enter host two secret password:")

#Host one config
Router_SSH = {
    "device_type": "cisco_ios",
    "host": host,
    "username": username,
    "password": password,
    "secret": secret,
    "port": 22,
    }

#Host two config
Switch_SSH = {
    "device_type": "cisco_ios",
    "host": host2,
    "username": username2,
    "password": password2,
    "secret": secret2,
    "port": 22,
    }

#Both hosts connect
net_connect_router = ConnectHandler(**Router_SSH)
net_connect_switch = ConnectHandler(**Switch_SSH)

#Script asks user if they would like to enebale loopback on host one
loopback_choice = input("Would you like to configure a loopback address on host one? Yes or No")
if loopback_choice.lower() == "yes":
    net_connect_router.enable()
    loopback_list = ['config t','interface loopback 0','ip address 10.0.0.1 255.255.255.0','exit']
    net_connect_router.send_config_set(loopback_list)

elif loopback_choice.lower() == "no":
    print("")

#Script asks user if they would like to enable RIP on host two
rip_choice = input("Would like you to configure RIP on host two? Yes or No")
if rip_choice.lower() == "yes":
    net_connect_switch.enable()
    rip_list = ['config t','router rip','no shutdown','network 10.0.0.1/24','exit']
    net_connect_switch.send_config_set(rip_list)

elif rip_choice.lower() == "no":
    print("")

vlan_choice = input("Would you like to configure a vlan on host two? Yes or No")
if vlan_choice.lower() == "yes":
    #VLAN choice inputs
    vlan_number = input("Which VLAN would you like to configure?")
    vlan_name = input("What would you like to name the VLAN?")
    vlan_ip = input("Please enter the ip address of the VLAN followed by the Subnet Mask")

    #Script sends commands to host two using the user inputs
    net_connect_switch.enable()
    vlan_list = ['config t','vlan '+ vlan_number,'name '+vlan_name,'ip address '+vlan_ip,'no shutdown','exit']
    net_connect_switch.send_config_set(vlan_list)

elif vlan_choice.lower() == "no":
    print("")
