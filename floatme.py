#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  floatme.py
#  
#  Copyright 2015 Arturo <arturo@papalinux>

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
floatme = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if not line.find ("0.8475") : continue
    count = count +1
    floatme = float(line[24:99])
    total = total + floatme 
    print floatme
print "Done"
