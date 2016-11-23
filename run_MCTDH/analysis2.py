#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************
# 	This PYTHON code finds maximum and minimum of each
#	coordinates as well as energy and writes them in 
#	a file called analysis.out

import sys
import os
import math

#----------------------------------------
#	This block for determining maximum and minimum for each column
#----------------------------------------
fin = open("train","r")
Ain = fin.readlines()
fin.close()
LN = len(Ain)

print "length of train set=",LN

for i in xrange(LN):
    ain = Ain[i].split()
    nod = len(ain)

trn,mn,rng = [],[],[]
for i in xrange(nod):
    trn.append([])
    rng.append(0.0)
    mn.append(0.0)

for i in xrange(LN):
    ain = Ain[i].split()
    if len(ain) > 0:
        for j in xrange(nod):
            trn[j].append(ain[j])

for i in xrange(nod):
    rng[i] = float(max(trn[i])) - float(min(trn[i]))
    mn[i] = float(min(trn[i]))

for i in xrange(nod):
    if mn[i] == 0.0:
        mn[i] = mn[i]+0.00001

#---------------------------------------
# This block is for calculating scaled "c"
#---------------------------------------

fc = open("HFCO.c","r")
C_old = fc.readlines()
fc.close()
c = C_old[0].split()[0]

fc_new = open("C","w")
cnew = float(c)*rng[nod-1]*0.50 + mn[nod-1] + 0.50*rng[nod-1]
fc_new.write(" %15.10f " %cnew)
fc_new.close()

#--------------------------------------
#	This block rescale weights (IW)
#--------------------------------------

f_iw_in = open("HFCO.IW","r")
IW_old = f_iw_in.readlines()
f_iw_in.close()
no_NN = len(IW_old) #nod-1 #len(IW_old[0].split())
print "NN=",len(IW_old)

iw_i = []
for i in xrange(no_NN):
    iw_j = []
    for j in xrange(nod-1):
        iw_j.append(0.0)
    iw_i.append(iw_j)
    
for i in xrange(no_NN):
    iw_old = IW_old[i].split()
    if len(iw_old) > 0:
        for j in xrange(nod-1):
            iw_i[i][j] = 2.0*float(iw_old[j])/rng[j]




f_iw_out = open("IW","w")
for i in xrange(no_NN):
    for j in xrange(nod-1):
        if j < (nod-2):
            f_iw_out.write("%20.10f "%iw_i[i][j])
        else:
            f_iw_out.write("%20.10f \n"%iw_i[i][j])

f_iw_out.close()
            






