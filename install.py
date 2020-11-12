import shutil, sys, os, control, git

hostname = sys.argv[1]
packname = 'pyabr'

## Get the latest version of Pyabr ##
cs = control.read_record('cs','etc/distro')

if not os.path.isdir ("desk/"+hostname):
	print ("Cannot install package; "+hostname+" host not found.")
	exit()

## Git ##
git.Git('pack/').clone(cs) # Git source code package # Helped from stockoverflow

if not os.path.isdir ("desk/"+hostname+"/pack"): os.mkdir ("desk/"+hostname+"/pack")
shutil.make_archive ('pack/'+packname,"zip",'pack/'+packname)
shutil.rmtree('pack/'+packname)
shutil.unpack_archive ("pack/"+packname+".zip","desk/"+hostname+"/pack","zip")
os.remove('pack/'+packname+".zip")
os.system ("cd desk/"+hostname+"/pack && python3 server.py")
shutil.make_archive ("desk/"+hostname+"/stor","zip","desk/"+hostname+"/pack/stor")
shutil.unpack_archive ("desk/"+hostname+"/stor.zip","desk/"+hostname+"/stor","zip")
os.remove ("desk/"+hostname+"/stor.zip")
shutil.rmtree ("desk/"+hostname+"/pack")
os.system ("chmod -R 777 desk/"+hostname+"/stor") # https://stackoverflow.com/questions/8328481/chmod-777-to-a-folder-and-all-contents
file = open ('desk/'+hostname+"/stor/etc/hostname",'w')
file.write (hostname)
file.close()