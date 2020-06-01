import os, sys, getpass

disk_name = sys.argv[1]
disk_size = sys.argv[2]

## Cannot create disk with xk ##
if not (disk_size.endswith("M") or disk_size.endswith("G") or disk_size.endswith("T")):
    print("Use: M, G or T for disk_size")
    exit()

## Cannot create disk lower than 12 MegaByte ##
if disk_size.endswith("M"):
    size = int(disk_size.replace("M", ""))
    if size < 12:
        print("Cannot create disk with " + disk_size + " size")
        exit()
    elif size > 1048576:
        print("Cannot create disk with " + disk_size + " size")
        exit()

if disk_size.endswith("G"):
    size = int(disk_size.replace("G", ""))
    if size > 1024:
        print("Cannot create disk with " + disk_size + " size")
        exit()

## Cannot create disk upper 1 TB ##
if disk_size.endswith("T"):
    size = int(disk_size.replace("T", ""))
    if size > 1:
        print("Cannot create disk with " + disk_size + " size")
        exit()

## Exists disk ##
if os.path.isfile("disk/" + disk_name):
    print("Cannot create disk; because " + disk_name + " has already exists.")
    exit()

os.system("qemu-img create disk/" + disk_name + " " + disk_size)