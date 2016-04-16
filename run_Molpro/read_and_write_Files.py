#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************

import glob
import math
import sys
import os

cpath = os.getcwd()
path = cpath+"/*.inp"
files=glob.glob(path)   
for file in files:
    f = open(file, "r+")
    a = f.readlines()
    N = len(a)
    print N
    f.close()
    f = open(file, "w")
    for i in range(0,N):
        s = a[i].split()
        if len(s) > 0 and s[0] =="rlxunit=cm-1,4501.1" and s[1] == "#" and s[2] == "Output":
            print "foundline"
            #break
            s[0] = "rlxunit=cm-1,4526.8780"
            #del s[1:4]
            a[i] = " ".join(str(x) for x in s)+'\n'
        f.write(a[i])

    f.close()

