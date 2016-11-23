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

#trn = [[],[],[],[],[],[],[]] # Empty list for train data sets, 
for i in xrange(5):
    ain = Ain[i].split()
    nod = len(ain)

trn,mn,rng = [],[],[]
for i in xrange(nod):
    trn.append([])
    rng.append(0.0)
    mn.append(0.0)


for i in xrange(5):
    ain = Ain[i].split()
    if len(ain) > 0:
        for j in xrange(7):
            trn[j].append(ain[j])
print "min r1=",min(trn[0])
#rng = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in xrange(nod):
    rng[i] = float(max(trn[i])) - float(min(trn[i]))
    mn[i] = float(min(trn[i]))

#---------------------------------------
# This block is for calculating scaled "c"
#---------------------------------------

fc = open("HFCO.c","r")
C_old = fc.readlines()
fc.close()
c = C_old[0].split()[0]

fc_new = open("C","w")
#cnew = float(max(trn[0])) - float(min(trn[0]))
cnew = float(c)*rng[nod-1]*0.50 + mn[nod-1] + 0.50*rng[nod-1]
fc_new.write(" %15.10f " %cnew)

print "cnew=",cnew

fc_new.close()




