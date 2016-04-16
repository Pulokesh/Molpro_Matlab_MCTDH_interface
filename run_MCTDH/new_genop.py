#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan, Alex Brown
#*
#******************************************************

#! /usr/bin/env python
import os
import math
from  numpy import *

path = "./"

label = "HFCO"
opfile = label+".op"
IW_file = open(path+"IW",'r') 
LW_file = open(path+"LW",'r')
rd_file = open(path+"rd",'r')
b_file = open(path+"b",'r')
c_file = open(path+"c",'r')
nofd = 6 #Number of degrees of freedom
nofn = 60 #Number of Neurons

IW_ini = []
IW = []
v = []
#coord = [3.446,2.488,2.4714,0.8619,-0.2519,3.14285] #here minimum TRANS of HFCO
coord = [2.0632,2.534,2.22874,-0.6138,-0.54038,3.14285] #coordinates of EQ HFCO

for i in range(nofn):
    IW.append("0")
    IW_ini.append("0")
    v.append("0")
   
cstr = c_file.readline()
clist = cstr.split()
c = clist[0]
LW_ini = LW_file.readline()
rd_ini = rd_file.readline()
b_ini = b_file.readline()

for i in range(nofn):
    IW_ini[i] = IW_file.readline()    
    IW[i] = IW_ini[i].split()

LW = LW_ini.split()
rd = rd_ini.split()
b = b_ini.split()

print len(LW)
print len(rd)
print len(b)

IW_file.close()
LW_file.close()
rd_file.close()
c_file.close()

op_file = open(path+opfile,'w')
op_file.write("PARAMETER-SECTION"+'\n')

for i in range(nofn):
    r = float(LW[i])*float(rd[i])*exp(float(b[i]))
    r_para = "r"+str(i)
    op_file.write(r_para+" = "+str(r)+'\n')
    for j in range(nofd):
	w = IW[i][j]
	op_file.write("w"+str(i)+"u"+str(j)+" = "+str(w)+'\n')
op_file.write("c = "+c+'\n')
op_file.write("end-parameter-section"+'\n')
op_file.write('\n')
op_file.write("LABELS-SECTION"+'\n')

for i in range(nofn):
    for j in range(nofd):
	ist = str(i)
	op_file.write("q"+str(i)+"u"+str(j)+" = exp[w"+str(i)+"u"+str(j)+",0.0]"+'\n')

op_file.write("end-labels-section"+'\n')
op_file.write('\n')
op_file.write("HAMILTONIAN-SECTION"+'\n')

op_file.write("-------------------------------------------------------------------------------"+'\n')

op_file.write("c"+"   |  1  |  1  |  1  |  1  |  1  |  1"+'\n')
for i in range(nofn):
    op_file.write("r"+str(i)+"     |  ")
    for j in range(nofd):	
	if (j == nofd -1):
	    op_file.write("q"+str(i)+"u"+str(j)+'\n')
	else:
	    op_file.write("q"+str(i)+"u"+str(j)+"  |  ")
op_file.write("-------------------------------------------------------------------------------"+'\n')
op_file.write("end-hamiltonian-section"+'\n')
op_file.close()

for i in range(nofn):
    v[i] = 1.0
    for j in range(nofd):
	v[i] = v[i]*exp(float(IW[i][j])*coord[j])

V = 0.0
for i in range(nofn):
    V = V + float(LW[i])*v[i]*exp(float(b[i]))*float(rd[i])
print V+float(c)
