
import os

if not os.path.isdir('desk'): os.mkdir ('desk')
if not os.path.isdir('disk'):os.mkdir ('disk')
if not os.path.isdir('pack'):os.mkdir ('pack')
if not os.path.isdir('etc'):os.mkdir('etc')
if not os.path.isdir('etc/hosts'):os.mkdir('etc/hosts')
file = open ('etc/distro','w')
file.write("""
name: Pyabr Server
version: 0.0.2
cs: https://github.com/manijamali2003/pyabr
""")
file.close()