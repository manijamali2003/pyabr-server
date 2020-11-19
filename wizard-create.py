import os, shutil, sys, hashlib,getpass, control

name = control.read_record ("name","etc/distro")
version = control.read_record ("version","etc/distro")

print ("Welcome to Remote Pyabr Service")
print (name+" "+version+" (c) 2020 Mani Jamali.")

hostname = input ("Enter your hostname: ")

if os.path.isdir ("/home/"+hostname):
	print ("Cannot create host; because "+hostname+" host has already exists.")
	exit(0)
	
os.system ("python3 create-host.py "+hostname)


disk_size = input ("Enter "+hostname+" host size {M,G,T}: ")

## Cannot create disk with xk ##
if not (disk_size.endswith("M") or disk_size.endswith("G") or disk_size.endswith("T")):
	print ("Use: M, G or T for disk_size")
	exit()

## Cannot create disk lower than 12 MegaByte ##
if disk_size.endswith ("M"):
	size = int(disk_size.replace("M",""))
	if size<12:
		print ("Cannot create disk with "+disk_size+" size")
		exit()
	elif size>1048576:
		print ("Cannot create disk with "+disk_size+" size")
		exit()
		
if disk_size.endswith ("G"):
	size = int(disk_size.replace("G",""))
	if size>1024:
		print ("Cannot create disk with "+disk_size+" size")
		exit()

## Cannot create disk upper 1 TB ##
if disk_size.endswith ("T"):
	size = int(disk_size.replace("T",""))
	if size>1:
		print ("Cannot create disk with "+disk_size+" size")
		exit()
		
os.system ("python3 create-disk.py "+hostname+" "+disk_size)
os.system ("python3 format-disk.py "+hostname)
os.system ("python3 active-host.py "+hostname)
os.system ("python3 install.py "+hostname)