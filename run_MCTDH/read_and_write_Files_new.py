#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************
##
# This script read and edit same file/files. Goes to the folder
# reads all the files with *.inp extension, reads them, edit specific 
# information, in this particular example, the ZPE, creates submission scripts
# for those individual input files such that when they are run, they goes to 
# different nodes at a time.

import glob   
import math
import sys
import os

path = '/home/ekadashi/HFCO/HFCO_full_PES/FULL_overfit_ct/NEW_cis/NEW_cis_reflect/EQ_mctdh/*.inp'   
files=glob.glob(path)   
for file in files:
    f = open(file, "r+")
    a = f.readlines()
    N = len(a)
    print N
    f.close()
    #ab4 = 4
    f = open(file, "w")
    for i in range(0,N):
        s = a[i].split()

        if len(s) > 0 and s[0] =="rch,ohco" and s[1] =="=":
            s[2] = "30"
            a[i] = " ".join(str(x) for x in s)+'\n' 

        if len(s) > 0 and s[0] =="rcf,ofco" and s[1] =="=":
            s[2] = "36"
            a[i] = " ".join(str(x) for x in s)+'\n'

        if len(s) > 0 and s[0] =="rco,phi" and s[1] =="=":
            s[2] = "28"
            a[i] = " ".join(str(x) for x in s)+'\n'

        if len(s) > 0 and s[0] =="rlxunit=cm-1,4526.8780" and s[1] == "#" and s[2] == "Output":
            print "foundline"
            s[0] = "rlxunit=cm-1,4526.820"
            a[i] = " ".join(str(x) for x in s)+'\n'
        f.write(a[i])

    f.close()

