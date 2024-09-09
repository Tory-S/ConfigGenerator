import tkinter as tk
from tkinter import *

nfh = open("New config.txt", "w")


def open_vlan_window():
    vlan_window = Toplevel()
    vlan_window.title("Extra window for VLANS")


def save_details():
    hostname = host_name.get()
    lan_address = lan_ip.get()
    wan_address = wan_ip.get()
    snmp_location = location.get()
    log_host = loghost.get()

    print("Router name: " + hostname)
    print("LAN IP: " + lan_address)
    print("WAN IP: " + wan_address)
    print("SNMP Location: " + snmp_location)
    print("Logging host: " + log_host)    

    fh = open("example_config.txt", mode="r")

    for line in fh:
        line = line.replace("< HOSTNAME >", str(hostname))
        line = line.replace("< LAN IP >", str(lan_address))
        line = line.replace("< WAN IP >", str(wan_address))
        line = line.replace("< SNMP LOCATION >", str(wan_address))
        nfh.write(line)

    
    nfh.close()



root = tk.Tk()
root.title("Create router config")

label1 = tk.Label(root, text="Hostname:")
label1.grid(row=0, column=0)

host_name = tk.Entry(root)
host_name.grid(row=0, column=1)

label2 = tk.Label(root, text="LAN IP:")
label2.grid(row=1, column=0)

lan_ip = tk.Entry(root)
lan_ip.grid(row=1, column=1)

label3 = tk.Label(root, text="WAN IP:")
label3.grid(row=2, column=0)

wan_ip = tk.Entry(root)
wan_ip.grid(row=2, column=1)

label4 = tk.Label(root, text="Device SNMP location:")
label4.grid(row=3, column=0)

location = tk.Entry(root)
location.grid(row=3, column=1)

label5 = tk.Label(root, text="Logging host:")
label5.grid(row=4, column=0)

loghost = tk.Entry(root)
loghost.grid(row=4, column=1)



do_stuff = tk.Button(root, text="Generate Config", command=save_details)
do_stuff.grid(row=5, column=0)

vlan_check = tk.Checkbutton(root,text="Additional VLAN config required",command=open_vlan_window)
vlan_check.grid(row=5, column=1)

root.mainloop()


