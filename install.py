import shutil, sys, os, control, git

hostname = sys.argv[1]
packname = 'pyabr'

## Get the latest version of Pyabr ##
cs = control.read_record('cs','etc/repo')

if not os.path.isdir ("desk/"+hostname):
	print ("Cannot install package; "+hostname+" host not found.")
	exit()

## Git ##
git.Git('pack/').clone(cs) # Git source code package # Helped from stockoverflow

if not os.path.isdir ("desk/"+hostname+"/pack"): os.mkdir ("desk/"+hostname+"/pack")
shutil.make_archive ('pack/'+packname,"zip",'pack/'+packname)
os.remove('pack/'+packname)
shutil.unpack_archive ("pack/"+packname+".zip","desk/"+hostname+"/pack","zip")
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

