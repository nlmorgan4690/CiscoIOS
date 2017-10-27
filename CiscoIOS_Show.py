"""
1. This scripts pulls in switches from the list1.csv file,  SSHs into each and runs a show command based off of the "output" variable.

2.  Library used is netmiko and this script utilizes the net_connect.send_command function.

--  Version 1.0
--  Dustin Bench, 8/25/17
--  Version 1.1 - Testing GitHub
--  Version 1.2 - still testing again and again and again and again 1 more time again
"""

import sys
from netmiko import ConnectHandler
from paramiko.ssh_exception import SSHException

file = open('c:\python27\list1.csv', 'r')

print '\n\n>>>>>>>>>>>>>>> Development Show Commands Python Script<<<<<<<<<<<<<<<<'
print '\n'


for line in file:
#Create a list out of list1.csv
    switch_list = line.strip().split(',')
#Place each line of list1 into a dictionary
    device_info = {}
    device_info['device_type'] = switch_list[1]
    device_info['ip'] = switch_list[2]
    device_info['username'] = switch_list[3]
    device_info['password'] = switch_list[4]
    #create python list that includes all of the items in the device_info dictionary
    all_devices = [device_info]
# Loop through device_info and apply config_commands to each element
    for a_device in all_devices:
        try:
            net_connect = ConnectHandler(**a_device)
            output = net_connect.send_command("show version")
            file2 = open('c:\\python27\showveroutput.txt', 'a+')
            file2.write("\n\n>>>>>>>>>>>>>>> Device {0} <<<<<<<<<<<<<<<".format(a_device['ip']) + '\n')
            file2.write(output)
            print "\n\n>>>>>>>>>>>>>>> Device {0} <<<<<<<<<<<<<<<".format(a_device['ip'])
            print output
        except SSHException:
            print "\n\n>>>>>>>>>>>>>>> Device {0} <<<<<<<<<<<<<<<".format(a_device['ip'])
            print 'Connection to device failed.  Please check TACACS configuration, exiting.'
            file3 = open('c:\\python27\tacacs.txt', 'a+')
            file3.write("\n\n>>>>>>>>>>>>>>> Device {0} <<<<<<<<<<<<<<<".format(a_device['ip']) + '\n')
            file3.write('Connection to device failed.  Please check TACACS configuration, exiting.' + '\n')
            continue
            sys.exit()
    print ">>>>>>>>>> END <<<<<<<<<<"
    
    
print "\n\n>>>>>>>>>>>>>>>>>>>>This is the end of the Script.  Good-bye<<<<<<<<<<<<<<<<<<<<<"
file.close()
file2.close()
file3.close()
