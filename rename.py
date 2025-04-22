#!/usr/bin/python2
# -*- coding: utf-8 -*-

#!/usr/bin/env python2
#
#  Copyright 2015 Arturo <arturo@papalinux>
import os
#import errno 
#import shutil 

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


for filename in filenames:
    os.rename(filename, filename.replace(" ", "-").replace('[','_').replace(']','_').replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n").lower()) 



