#!/usr/bin/python2
# -*- coding: utf-8 -*-

#!/usr/bin/env python2
#
#  jsongoogleapi.py
#  
#  Copyright 2015 Arturo <arturo@papalinux>
import os
import shutil 

""" 
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens and standarize some other characters
(2) Makes lowercase (not a Unix requirement, just looks better ;)
(3) Sort series to the right folder
Usage:
python sortrename.py
"""

#path =  os.getcwd()
path = "/avi/cosas/0-Unsorted"
path_sorted = "/avi/0-New/Sorted"
path_new = "/avi/0-New"
filenames = os.listdir(path)

# renames files & folders as well as replace ' ' with _ and special characters

path = "/avi/cosas/0-Unsorted"

def lowercase_rename( dir ):
    # renames all subforders of dir, not including dir itself
    def rename_all( root, items):
        for name in items:
            try:
                os.rename( os.path.join(root, name), 
                                    os.path.join(root, name.replace(" ", "-").replace('[','_').replace(']','_').replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n").lower()))
            except OSError:
                pass # can't rename it, so what

    # starts from the bottom so paths further up remain valid after renaming
    for root, dirs, files in os.walk( dir, topdown=False ):
        rename_all( root, dirs )
        rename_all( root, files)

lowercase_rename(path)


       
filenames = os.listdir(path)
series = [ 'walking.dead','izombie','sherlock','sleepy.hollow','legends','mike','big.bang','blindspot','bones','carlos','castle','code.black','elementary','grimm','mysteries.of.laura','last.kingdom','z.nation','shameless.us']
for filename in filenames:
    for serie in series:
        if serie in filename:
            if os.path.isdir(filename):
                filenames2 = os.listdir(filename)
                for subserie in filenames2:
                    source2 = str(path+"/"+filename+"/"+subserie)
                    destino = str(path_sorted+"/"+serie+"/"+subserie)
                    try :
                        shutil.move(source2, destino)
                    except:
                        print "error moving"
                        continue
                    try: os.rmdir(filename)
                    except OSError as ex:
                        if ex.errno == errno.ENOTEMPTY:
                            print "directory not empty"
                
        elif serie in filename:
            source1 = path+"/"+str(filename)
            target1 = str(path_sorted+"/"+serie+"/"+filename)
            print source1, target1
            try :shutil.move(source1, target1)
            except :print "move failed"
			

#move to 0-New anthing that could not be sorted
filenames = os.listdir(path)
for filename in filenames:
    source1 = path+"/"+str(filename)
    target1 = str(path_new+"/"+filename)
#    print source1, target1    
    shutil.move(source1, target1)


