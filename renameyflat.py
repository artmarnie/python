#!/usr/bin/python2
# -*- coding: utf-8 -*-

#!/usr/bin/env python2
#
#  Copyright 2015 Arturo <arturo@papalinux>
import os
import errno 
import shutil 

""" 
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens and standarize some other characters
(2) Makes lowercase (not a Unix requirement, just looks better ;)
Usage:
python rename.py
"""

#path =  os.getcwd()
path = "/avi/cosas/0-Unsorted"
path_sorted = "/avi/0-New/Sorted"
path_new = "/avi/0-New"
filenames = os.listdir(path)

# renaming stuff
def lowercase_rename( dir ):
    # renames all subforders of dir, not including dir itself
    def rename_all( root, items):
        for name in items:
            try:
                os.chmod(os.path.join(root, name),0777)
                os.rename( os.path.join(root, name), os.path.join(root, name.replace(" ", "-").replace('[','_').replace(']','_').replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n").lower()))
            except :print "error renaming"
             #   pass # can't rename it, so what

    # starts from the bottom so paths further up remain valid after renaming
    
    for root, dirs, files in os.walk( dir, topdown=False ):
        rename_all( root, dirs )
        rename_all( root, files)

lowercase_rename(path)

# copy all the files in the subfolders to main folder
 
# The current working directory
dest_dir = "/avi/cosas/0-Unsorted"
#dest_dir = os.getcwd()
# The generator that walks over the folder tree
walker = os.walk(dest_dir)
 
# the first walk would be the same main directory
# which if processed, is
# redundant
# and raises shutil.Error
# as the file already exists
 
rem_dirs = walker.next()[1]
 
for data in walker:
	for files in data[2]:
		try :shutil.move(data[0] + os.sep + files, dest_dir)
		except shutil.Error:
			continue
 
# clearing the directories
# from whom we have just removed the files
for dirs in rem_dirs:
	shutil.rmtree(dest_dir + os.sep + dirs)

