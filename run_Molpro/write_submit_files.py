#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************

import glob   
import math
import sys
import os

cpath = os.getcwd()
path = cpath+"/*.mpi"

files=glob.glob(path)   
N = len(files)
print N
fi = open("submit_tmpl.pbs","r")
fsub = open("sim_submit.sh", "w")
fa = fi.readlines()
nfa = len(fa)
fi.close()
for file in files:
    print file
    af = file.split('/')
    print af[10]
    sa = af[10].split('.')
    saa = sa[0]
    f = open("molpro_%s.pbs" %af[10], "w")
    for j in range(0,nfa):
        f.write(fa[j])
    f.write("\n")
    f.write("molpro -v -m 5000m -S ga %s \n" %af[10])
    #f.write("os.system(\"rm molpro_%s.pbs.* %s.xml %s.out\") \n" %(af[10], saa, saa))


    fsub.write("qsub molpro_%s.pbs \n" %af[10])
    f.close()    
fsub.close()

