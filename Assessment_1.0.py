from netmiko import ConnectHandler

Router_Telnet = {
    "device_type": "cisco_ios_telnet",
    "host": "10.10.10.5",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}

Router_SSH = {
    "device_type": "cisco_ios",
    "host": "10.10.10.5",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    "port": 22,
}

choice = input("Would you like to connect via telnet or ssh?")

if choice == "telnet" or "Telnet":
    telnet_connect = ConnectHandler(Router_Telnet)

elif choice == "ssh" or "SSH":
    ssh_connect = ConnectHandler(Router_SSH)
    backup_config = open("config.txt", "w")
    enable_router = ssh_connect.enable()
    output = ssh_connect.send_command("show running-config")
    backup_config.write(output)
    backup_config.close()
