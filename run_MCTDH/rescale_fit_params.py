#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************
#
# 	This PYTHON code generates rescaled parameters IW, b, c, rd
#	later used in new_genop.py code to generate MCTDH operator file
#
#-----------------------------------------------------

import sys
import os
import math

#---------------------------------------
#	First copy HFCO.LW, HFCO.b to LW and b respectively. 
#	These are later used as input for new_genop.py
#---------------------------------------

os.system("cp HFCO.LW LW")
os.system("cp HFCO.b b")

#----------------------------------------
#	This block is for determining maximum and minimum for each column (coordinates and energy)
#----------------------------------------

f_in = open("train","r")
Ain = f_in.readlines()
f_in.close()
LN = len(Ain)

print "length of train set=",LN

for i in xrange(LN):
    ain = Ain[i].split()
    nod = len(ain)     # number of columns

trn,mn,rng = [],[],[] #creating empty list of train, minimum, range (=max-min)
for i in xrange(nod):
    trn.append([])
    rng.append(0.0)
    mn.append(0.0)

for i in xrange(LN):
    ain = Ain[i].split()
    if len(ain) > 0:
        for j in xrange(nod):
            trn[j].append(float(ain[j]))

for i in xrange(nod):
    rng[i] = max(trn[i]) - min(trn[i])
    mn[i] = min(trn[i])

#---------------------------------------
# This block is for calculating rescaled "c"
#---------------------------------------

fc_in = open("HFCO.c","r")
C_old = fc_in.readlines()
fc_in.close()
C = C_old[0].split()[0]

fc_new = open("c","w")
cnew = float(C)*rng[nod-1]*0.50 + mn[nod-1] + 0.50*rng[nod-1]
fc_new.write(" %15.10f " %cnew)
fc_new.close()

#--------------------------------------
#	This block rescale weights (IW)
#	new set of parameters, called rd
#--------------------------------------

f_iw_in = open("HFCO.IW","r")
IW_old = f_iw_in.readlines()
f_iw_in.close()
no_NN = len(IW_old) # number of Neurons
print "NN=",len(IW_old)

iw_i = []
for i in xrange(no_NN):
    iw_j = []
    for j in xrange(nod-1):
        iw_j.append(0.0)
    iw_i.append(iw_j)
    
f_rd = open("rd","w")
for i in xrange(no_NN):
    iw_old = IW_old[i].split()
    if len(iw_old) > 0:
        d1 = 1.0
        for j in xrange(nod-1):
            iw_i[i][j] = 2.0*float(iw_old[j])/rng[j]
            #d2 = 2.0*float(iw_old[j])*mn[j]/rng[j] + float(iw_old[j])
            d1 = d1*math.exp(-1.0*(2.0*float(iw_old[j])*mn[j]/rng[j] + float(iw_old[j])))
            #d3 = math.exp(-1.0*d2)
            #d1 = d3*d1
        d2 = d1*0.50*rng[nod-1]
        f_rd.write("%32.15f "%d2)
f_rd.close()

f_iw_out = open("IW","w")
for i in xrange(no_NN):
    for j in xrange(nod-1):
        if j < (nod-2):
            f_iw_out.write("%20.10f "%iw_i[i][j])
        else:
            f_iw_out.write("%20.10f \n"%iw_i[i][j])

f_iw_out.close()
 

