import os, sys, shutil

hostname = sys.argv[1]

if not os.path.isdir ("desk/"+hostname):
	print ("Cannot active host; because host not found.")
	exit()
	
if os.path.isdir ("desk/"+hostname+"/stor"):
	print ("Cannot active host; because host has already actived.")
	exit()

os.mkdir ("desk/"+hostname+"/stor")
os.system ("mount disk/"+hostname+" desk/"+hostname+"/stor")
