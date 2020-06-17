
import os

os.mkdir ('desk')
os.mkdir ('disk')
os.mkdir ('pack')
os.mkdir('etc')
os.mkdir('etc/hosts')
file = open ('etc/distro','w')
file.write("""
name: Pyabr Server
version: 0.0.2
cs: https://github.com/manijamali2003/pyabr
""")
file.close()