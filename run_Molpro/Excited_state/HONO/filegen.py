#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************
#! /usr/bin/env python
import os
import math
import sys
from  numpy import *

path = "./"

coord_file = open(path+"coord",'r') 
file_tot = coord_file.readlines()
nofk = len(file_tot)
coord_file.close()
print "num of rows=",nofk
#sys.exit(0)
coord_ini = [] 
coord = [] 
##################
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
    f.write("***,HONO S0 surf CASSCF conputation"+'\n')
    f.write("print,orbitals,civector"+'\n')
    f.write('\n')
    f.write("memory,300,m"+'\n')
    f.write('\n')
    f.write("symmetry,nosym"+'\n')
    f.write("geometry={H;"+'\n')
    f.write("O,H,r2;"+'\n')
    f.write("N,O,r1,H,r4;"+'\n')
    f.write("O,N,r0,O,r3,H,r5}"+'\n')
    f.write('\n')


    for j in range(nofdd):
        #print i,j
        w = coord[i][j]
        f.write("r"+str(j)+" = "+str(w)+'\n')
    f.write('\n')
    f.write("basis=avtz;"+'\n')
    f.write("hf;"+'\n')
#    f.write("mp2;"+'\n')
#    f.write("natorb,2101.2;"+'\n')
    f.write("{casscf;"+'\n')
    f.write("closed,3;occ,16;"+'\n')
    f.write("wf,24,1,0;state,2;"+'\n')
    f.write("wf,24,1,2;state,1}"+'\n')
#    f.write("start,2101.2;"+'\n')
#    f.write("orbital,2140.2}"+'\n')
    f.write("ecas1=energy(1)"+'\n')
    f.write("ecas2=energy(2)"+'\n')
    f.write("ecas3=energy(3)"+'\n')
#    f.write("{mrci-f12,singles=0"+'\n')
#    f.write("wf,24,1,0;state,1}"+'\n')
#    f.write("emrcd1=energd"+'\n')
    f.write('\n')
    f.write("{table,r0,r1,r2,r3,r4,r5,ecas1,ecas2,ecas3"+'\n')
    f.write("head,rN=O,rON,rOH,aONO,aHON,aphi,ecas1,ecas2,ecas3"+'\n')
    f.write("save,table_1D_cuts.out"+'\n')
    f.write("title,Results HONO S0 surf CASSCF cal"+'\n')
    f.write("}"+'\n')
    f.write("---"+'\n')

#######################Modification being done    
