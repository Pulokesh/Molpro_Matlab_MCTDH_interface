#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************
#from numpy.oldnumeric import *
#from numpy.oldnumeric.linear_algebra import *
import numpy
from numpy import *

import os


output = open("table.out", "r")
# initialize variables to zero (good practice)
gradArray = zeros((100, 100), float)
# initializes a 3-vector of Floats
gradVector = zeros(10,float)
foundGrad = 0
foundLine=0

energyFile = open("energy", 'w')
energyFile = open("energy", 'a') # append
# python shorthand
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
#               gradVector[1] = float(temp[5])
#               gradVector[2] = float(temp[8])

                 energyFile.write(str(gradVector[0])+" "+str(gradVector[1])+" "+str(gradVector[2])+" "
                  +str(gradVector[3])+" "+str(gradVector[4])+" "+str(gradVector[5])+" "+str(gradVector[6])
                  +" "+str(gradVector[7])+'\n')
#                 if((temp[0]=="SETTING") and (temp[4] == "AU")):
#                        foundLine = 1
#                        continue # go to next iteration
#	if(foundLine == 2):
#		print 'okay'
#		temp = line.split()
#	 	if(len(temp) == 5):
#		 print 'okay'
#		gradVector[0] = float(temp[3])
#		gradVector[1] = float(temp[5])
#		gradVector[2] = float(temp[8])
		
#                dipoleFile.write(str(gradVector[0]) + "\n")
#                dipoleFile.write(str(gradVector[0]) + " " + str(gradVector[1]) + " " + str(gradVector[2]) + "\n")
 	        foundLine =0

#dipoleFile = open("dipoles", 'w')
#dipoleFile = open("dipoles", 'a') # append
#dipoleFile.write(str(gradVector[0]) + " " + str(gradVector[1]) + " " + str(gradVector[2]) + "\n")
#dipoleFile = open("dipoles", 'a') # append






output.close()




