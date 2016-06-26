#*****************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************
#
#! /usr/bin/env python
import os
import math
import sys
from  numpy import *

path = "./"

coord_file = open(path+"coord",'r') 
tmp_file = open(path+"input_templ",'r')

file_tot = coord_file.readlines()
nofk = len(file_tot)
coord_file.close()
print "num of rows=",nofk
coord_ini = [] 
coord = [] 

lt = tmp_file.readlines()
nt = len(lt)
print "#lines of templ file=",nt

for tn in xrange(nt):
    tw = lt[tn].split()
    if len(tw)!=0 and tw[0] == "r0":
        ntup = tn
    elif len(tw)!=0 and tw[0] == "r5" :
        ntdn = tn + 1

print "coord statr=",ntup,"coord_end=",ntdn
for i in range(nofk):
    coord.append("0") 
    coord_ini.append("0") 

coord_file = open(path+"coord",'r') 
for k in range(nofk):                     
    coord_ini[k] = coord_file.readline()  
    coord[k] = coord_ini[k].split()       
nofdd = len(coord_ini[0].split())
print "num of column=",nofdd


for i in range(nofk):
    f = open("input_%i.mpi" %i,'w')

    for ja in range(0,ntup):
        f.write(lt[ja])
    f.write('\n')

    for j in range(nofdd):
        #print i,j
        w = coord[i][j]
        f.write("r"+str(j)+" = "+str(w)+'\n')
    f.write('\n')

    for jb in range(ntdn,tn+1):
        f.write(lt[jb])
    f.write('\n')

