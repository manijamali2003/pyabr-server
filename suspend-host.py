import os, sys, shutil

hostname = sys.argv[1]

if not os.path.isdir ("desk/"+hostname):
	print ("Cannot suspend host; because host not found.")
	exit()
	
if not os.path.isdir ("desk/"+hostname+"/stor"):
	print ("Cannot suspend host; because host has already suspended.")
	exit()


os.system ("umount disk/"+hostname)
os.rmdir ("desk/"+hostname+"/stor")
