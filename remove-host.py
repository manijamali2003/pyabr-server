import os, sys, shutil

hostname = sys.argv[1]

if not os.path.isdir ("/home/"+hostname):
	print ("Cannot remove host; because "+hostname+" host not found.")
	exit(0)

os.system ("userdel "+hostname)
shutil.rmtree ("/home/"+hostname)
os.remove ("desk/"+hostname)
