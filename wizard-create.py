import os, shutil, sys, hashlib,getpass, control

name = control.read_record ("name","etc/distro")
version = control.read_record ("version","etc/distro")

print ("Welcome to PyServer")
print (name+" "+version+" (c) 2020 Mani Jamali.")

hostname = input ("Enter your hostname: ")

if os.path.isdir ("/home/"+hostname):
	print ("Cannot create host; because "+hostname+" host has already exists.")
	exit(0)
	
os.system ("python create-host.py "+hostname)


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
		
os.system ("python create-disk.py "+hostname+" "+disk_size)
os.system ("python format-disk.py "+hostname)
os.system ("python active-host.py "+hostname)
os.system ("python install.py "+hostname)

while True:
	root_password = getpass.getpass ("Enter your new root password: ")
	confirm_root = getpass.getpass ("Confirm your new root password: ")
	
	if root_password==confirm_root: break
	else: print ("Try again!")
	
username = input ("Enter your username: ")

while True:
	user_password = getpass.getpass ("Enter your new user password: ")
	confirm_user = getpass.getpass ("Confirm your new user password: ")
	
	if user_password==confirm_user: break
	else: print ("Try again!")
	
first_name = input ("Enter your first name: ")
last_name = input ("Enter your last name: ")
phone = input ("Enter your phone number: ")
email = input ("Enter your email address: ")
interface = input ("Choose your interface (CLI/GUI): ").upper()
if interface==None: interface=="CLI"
guest = input ("Do you want to enable guest user? [Y/n]: ").upper()
if guest=="Y": guest="Yes"
else: guest=="No"

file = open ("desk/"+hostname+"/stor/etc/users/root","w")
file.write ("username: "+hashlib.sha3_256(str("root").encode()).hexdigest()+"\n")
file.write ("code: "+hashlib.sha3_512(str(root_password).encode()).hexdigest()+"\n")
file.close()

file = open ("desk/"+hostname+"/stor/etc/users/"+username,"w")
file.write ("username: "+hashlib.sha3_256(str(username).encode()).hexdigest()+"\n")
file.write ("code: "+hashlib.sha3_512(str(user_password).encode()).hexdigest()+"\n")
file.write ("first_name: "+first_name+"\n")
file.write ("last_name: "+last_name+"\n")
file.write ("email: "+email+"\n")
file.write ("phone: "+phone+"\n")
file.close()

file = open ("desk/"+hostname+"/stor/etc/guest","w")
file.write ("enable_cli: "+guest+"\n")
file.write ("enable_gui: "+guest+"\n")
file.close()

file = open ("desk/"+hostname+"/stor/etc/interface","w")
file.write (interface)
file.close()

file = open ("desk/"+hostname+"/stor/etc/permtab","a")
file.write ("/desk/"+username+": rwxr-x---\n")
file.close()

file = open ("etc/hosts/"+hostname,"w")
file.write ("hostname: "+hashlib.sha3_256(str(hostname).encode()).hexdigest()+"\n")
file.write ("username: "+hashlib.sha3_256(str(username).encode()).hexdigest()+"\n")
file.write ("phone: "+hashlib.sha3_256(str(phone).encode()).hexdigest()+"\n")
file.write ("email: "+hashlib.sha3_256(str(hostname).encode()).hexdigest()+"\n")
file.write ("first_name: "+hashlib.sha3_256(str(first_name).encode()).hexdigest()+"\n")
file.write ("last_name: "+hashlib.sha3_256(str(last_name).encode()).hexdigest()+"\n")
file.close()
