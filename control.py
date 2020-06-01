import os

def read_record (name,filename):
    file = open (filename,"r")
    strv = file.read()
    file.close()
    strv = strv.split("\n")

    for i in strv:
        if i.startswith(name):
            i = i.split(": ")
            if i[0]==(name):
                return i[1]

def read_list (filename):
    file = open (filename,"r")
    strv = file.read()
    file.close()
    strv = strv.split("\n")
    return strv