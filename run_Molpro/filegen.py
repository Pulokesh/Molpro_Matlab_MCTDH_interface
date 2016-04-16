#*****************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************

#! /usr/bin/env python
import os
import math
from  numpy import *

path = "./"

coord_file = open(path+"coord",'r') # coord file needs to be present in the same directory
nofd = 9 #Number of degrees of freedom
nofdd = nofd - 3
#nofn = 280 #Number of terms (Neurons)
nofk = 75 #input the data of external file here

coord_ini = [] 
coord = [] 

for i in range(nofk):
    coord.append("0") 
    coord_ini.append("0") 

for k in range(nofk):                     
    coord_ini[k] = coord_file.readline()  
    coord[k] = coord_ini[k].split()       


for i in range(nofk):
    f = open("input_%i.mpi" %i,'w')
    f.write("***,HFCO S1 surf CASSCF conputation"+'\n')
    f.write('\n')
    f.write("memory,300,m"+'\n')
    f.write('\n')
    f.write("symmetry,nosym"+'\n')
    f.write("geometry={C;"+'\n')
    f.write("O,C,r2;"+'\n')
    f.write("H,C,r0,O,r3;"+'\n')
    f.write("F,C,r1,O,r4,H,r5}"+'\n')
    f.write('\n')
    for j in range(nofdd):
        w = coord[i][j]
        f.write("r"+str(j)+" = "+str(w)+'\n')
    f.write('\n')
    f.write("basis=avtz;"+'\n')
    f.write("hf;"+'\n')
    f.write("{multi;maxit,40;"+'\n')
    f.write("closed,3;occ,15;"+'\n')
    f.write("wf,24,1,0;state,2}"+'\n')
    f.write("ecas1=energy(1)"+'\n')
    f.write("ecas2=energy(2)"+'\n')

    # Following options for MRCI calculations
    #f.write("{mrci-f12,singles=0"+'\n')
    #f.write("wf,24,1,0;state,1}"+'\n')
    #f.write("emrcd1=energd"+'\n')
    f.write('\n')
    f.write("{table,r0,r1,r2,r3,r4,r5,ecas1,ecas2"+'\n')
    f.write("head,rch,rcf,rcf,ahco,afco,aphi,ecas1,ecas2"+'\n')
    f.write("save,table_1D_cuts.out"+'\n')
    f.write("title,Results HFCO S1 surf CASSCF cal"+'\n')
    f.write("}"+'\n')
    f.write("---"+'\n')

