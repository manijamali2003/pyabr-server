import os, sys

hostname = sys.argv[1]

if os.path.isdir ("/home/"+hostname):
	print ("Cannot create host; because "+hostname+" host has already exists.")
	exit(0)

os.system ("useradd "+hostname+" -m")
os.system ("passwd "+hostname)
os.system ("ln -sv /home/"+hostname+" desk/"+hostname)


activate = '''
#!/bin/python

import os, sys
def run():
	os.system ("cd stor && python3 vmnam.pyc")
'''

check_activation = '''
#!/bin/python

import os, activate

os.system ("clear")

if not os.path.isdir ("stor"):
	print ("This host has already suspended.")
else:
	activate.run()
'''

bashrc = '''
python3 check-activation.py
exit
'''

file = open ("desk/"+hostname+"/.bashrc","w")
file.write (bashrc)
file.close()

file = open ("desk/"+hostname+"/.profile","w")
file.write (bashrc)
file.close()

file = open ("desk/"+hostname+"/activate.py","w")
file.write (activate)
file.close()

file = open ("desk/"+hostname+"/check-activation.py","w")
file.write (check_activation)
file.close()
