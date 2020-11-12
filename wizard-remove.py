import shutil, os, sys, control

name = control.read_record ("name","etc/distro")
version = control.read_record ("version","etc/distro")

print ("Welcome to PyServer")
print (name+" "+version+" (c) 2020 Mani Jamali.")

hostname = input ("Enter your hostname: ")

if not os.path.isdir ("desk/"+hostname):
	print ("Cannot remove host; because host not found.")
	exit()
	
if not os.path.isfile ("disk/"+hostname):
	print ("Cannot remove disk; because disk not found.")
	exit()
	
if os.path.isdir ("desk/"+hostname+"/stor"):
	os.system ("python3 suspend-host.py "+hostname)
	
os.system ("python3 remove-disk.py "+hostname)
os.system ("python3 remove-host.py "+hostname)