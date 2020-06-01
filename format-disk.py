import os, sys

disk_name = sys.argv[1]

os.system ("mkfs.ext4 disk/"+disk_name)
