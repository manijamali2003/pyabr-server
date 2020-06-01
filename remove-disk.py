import os, sys

disk_name = sys.argv[1]

if not os.path.isfile ("disk/"+disk_name):
	print ("Cannot remove disk; because "+disk_name+" disk not found.")
	exit()
	
os.remove ("disk/"+disk_name)
