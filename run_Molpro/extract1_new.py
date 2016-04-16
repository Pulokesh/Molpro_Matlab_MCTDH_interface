#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************

import numpy
from numpy import *

import os
import glob
import math
import sys

cpath = os.getcwd()
path = cpath+"/table*.out"

files=glob.glob(path)
N = len(files)
print N
#sys.exit(0)
energyFile = open("energy", 'w')
energyFile = open("energy", 'a') # append

for i in range(0,2):
    
    output = open("table%i_1d_cuts.out" %i , "r")
# initialize variables to zero (good practice)
    gradArray = zeros((100, 100), float)
# initializes a 3-vector of Floats
    gradVector = zeros(10,float)
    foundGrad = 0
    foundLine=0

# python sorting
    for line in output:
	if(foundLine == 0):
            temp = line.split()
            if(len(temp) == 8):
	        if((temp[0]=="RCH") and (temp[7] == "ECAS2")):
		    foundLine = 1
		    continue # go to next iteration
        if(foundLine == 1):
            temp = line.split()
            if(len(temp) == 8):
	        print 'okay'
                gradVector[0] = float(temp[0])
                gradVector[1] = float(temp[1])
                gradVector[2] = float(temp[2])
                gradVector[3] = float(temp[3])
                gradVector[4] = float(temp[4])
                gradVector[5] = float(temp[5])
                gradVector[6] = float(temp[6])
                gradVector[7] = float(temp[7])

                energyFile.write(str(gradVector[0])+" "+str(gradVector[1])+" "+str(gradVector[2])+" "
                  +str(gradVector[3])+" "+str(gradVector[4])+" "+str(gradVector[5])+" "+str(gradVector[6])
                  +" "+str(gradVector[7])+'\n')
 	        foundLine =0

output.close()




