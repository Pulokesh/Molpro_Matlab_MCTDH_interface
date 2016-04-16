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

path = '/home/ekadashi/HFCO/HFCO_paper_review/30k_cut_PES/Random_1D/100N/*.inp'   
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
        if len(s) > 0 and s[0] =="rlxunit=cm-1,4501.1" and s[1] == "#" and s[2] == "Output":
            print "foundline"
            s[0] = "rlxunit=cm-1,4526.8780"
            a[i] = " ".join(str(x) for x in s)+'\n'
        f.write(a[i])

    f.close()

