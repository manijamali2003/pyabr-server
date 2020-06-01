import shutil, sys, os

packname = sys.argv[1]
hostname = sys.argv[2]

if not os.path.isfile ("pack/"+packname):
	print ("Cannot install package; "+package+" package not found.")
	exit()
	
if not os.path.isdir ("desk/"+hostname):
	print ("Cannot install package; "+hostname+" host not found.")
	exit()
	
if not os.path.isdir ("desk/"+hostname+"/pack"): os.mkdir ("desk/"+hostname+"/pack")

shutil.unpack_archive ("pack/"+packname,"desk/"+hostname+"/pack","zip")
file = open ("desk/"+hostname+"/pack/config/password.txt","w")
file.write ("toor")
file.close()
file = open ("desk/"+hostname+"/pack/config/hostname.txt","w")
file.write (hostname)
file.close()
os.system ("cd desk/"+hostname+"/pack && python build.py && python build-config.py")
shutil.make_archive ("desk/"+hostname+"/stor","zip","desk/"+hostname+"/pack/stor")
shutil.unpack_archive ("desk/"+hostname+"/stor.zip","desk/"+hostname+"/stor","zip")
os.remove ("desk/"+hostname+"/stor.zip")
shutil.rmtree ("desk/"+hostname+"/pack")
os.system ("chmod -R 777 desk/"+hostname+"/stor") # https://stackoverflow.com/questions/8328481/chmod-777-to-a-folder-and-all-contents

