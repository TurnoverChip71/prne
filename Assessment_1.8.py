from netmiko import ConnectHandler

choice = input("Would you like to connect via telnet or ssh?")

if choice == "telnet" or "Telnet":
     host = input("Please enter host ip address:")
     username = input("Please enter username:")
     password = input("Please enter password:")
     secret = input("Please enter secret password:")
     
     Router_Telnet = {
     "device_type": "cisco_ios_telnet",
     "host": host,
     "username": username,
     "password": password,
     "secret": secret,
     }
     
     telnet_connect = ConnectHandler(Router_Telnet)

elif choice == "ssh" or "SSH":
    host = input("Please enter host ip address:")
    username = input("Please enter username:")
    password = input("Please enter password:")
    secret = input("Please enter secret password:")
    conf_choice = input("Would you like to backup the config? Yes or No:")
    
    Router_SSH = {
    "device_type": "cisco_ios",
    "host": host,
    "username": username,
    "password": password,
    "secret": secret,
    "port": 22,
    }

    if conf_choice == "Yes" or "yes":
        file_name = input("What would you like the file to be named(Include .txt):")
        ssh_connect = ConnectHandler(Router_SSH)
        backup_config = open(file_name, "w")
        enable_router = ssh_connect.enable()
        output = ssh_connect.send_command("show running-config")
        backup_config.write(output)
        backup_config.close()
        print("Config backed up!")

    elif conf_choice == "No" or "no":
        ssh_connect = ConnectHandler(Router_SSH)