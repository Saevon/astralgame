from os import *
from time import ctime

def get_file_dir(cur_dir = getcwd(), ext = "all"):
    chdir(cur_dir)
    while 1:
        print cur_dir
        print "(Type Cancel to quit)\n"
        if path.isfile(cur_dir):
            path.chdir(path.dirname(cur_dir))
            return path.basename(cur_dir)
        all_items = listdir(cur_dir)
        files, directories = [],[]
        for item in all_items:
            if path.isdir(item):
                directories.append(item)
            else:files.append(item)
        files.sort()
        directories.sort()
        for item in directories:
            print "+  " + item
        print ""
        for item in files:
            if ext == "all" or item.endswith(ext):
                print item[:item.find(".")] + " " * (30 - len(item[:item.find(".")])) + ctime(path.getmtime(item))
        temp = raw_input(": ")
        if path.exists(temp) and path.isfile(temp):
            return temp
        if path.exists(temp + ext) and path.isfile(temp + ext):
            return temp + ext
        if temp == "cancel":
            break
        
            
        
        
        
"""
normcase(s) #makes into lowercase, and all backslashes
exists(s) #does it exist, possibel fielname
irname(p) # returns the dir component
basename(s) # retunrns the file component

get_file_dir("G:\Astral", ext = ".sav")
"""