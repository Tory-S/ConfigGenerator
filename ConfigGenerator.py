import tkinter as tk

nfh = open("New config.txt", "w")





def save_details():
    hostname = host_name.get()
    lan_address = lan_ip.get()
    wan_address = wan_ip.get()
    snmp_location = location.get()

    print("Router name: " + hostname)
    print("LAN IP: " + lan_address)
    print("WAN IP: " + wan_address)
    print("SNMP Location: " + snmp_location)

    fh = open("example_config.txt", mode="r")

    for line in fh:
        line = line.replace("< HOSTNAME >", str(hostname))
        line = line.replace("< LAN IP >", str(lan_address))
        line = line.replace("< WAN IP >", str(wan_address))
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

do_stuff = tk.Button(root, text="Generate Config", command=save_details)
do_stuff.grid(row=4, column=0)



root.mainloop()


