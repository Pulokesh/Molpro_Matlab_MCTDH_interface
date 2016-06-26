#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************
#
#! /usr/bin/env python
import os
import math
from  numpy import *


nofk = 6 # number of input files


f = open("molpro.pbs" ,'w')
#f.write(" "+"***,HONO mrci F12 conputation"+'\n')
#f.write('\n')
f.write("#!/bin/bash"+'\n')
f.write("#PBS -S /bin/bash"+'\n')
f.write("#PBS -l walltime=02:00:00"+'\n')
f.write("#PBS -l pmem=8gb,procs=8,file=24gb"+'\n')
f.write("#PBS -m bea"+'\n')
f.write("#PBS -r n"+'\n')
f.write('\n')
f.write("cd $PBS_O_WORKDIR"+'\n')
f.write("echo \"Current working directory is `pwd`\" "+'\n')
f.write("echo \"Starting run at: `date`\" "+'\n')
f.write('\n')
f.write("echo \"my PBS_NODEFILE contains:\""+'\n')
f.write("cat $PBS_NODEFILE"+'\n')
f.write('\n')
f.write("#Create Scratch directory"+'\n')
f.write("#SCRATCHDR=/global/scratch/$USER/${PBS_JOBID}"+'\n')
f.write("#mkdir $SCRATCHDR"+'\n')
f.write("#cd $SCRATCHDR"+'\n')
f.write('\n')
f.write("# GAS seems that for GA version, shared filesystem is not needed."+'\n')
f.write("# so it does not have to be in $SCRATCHDIR ; I've used $TMPDIR"+'\n')
f.write("# as proviede by Torque. The only question is where would it put incomplete"+'\n')
f.write("# files good for restarts? Is this TMPDIR4? Or current WORKDIR?"+'\n')
f.write("# perhaps one sould use -I and -W flags to molpro command to store the data"+'\n')
f.write("# somewhere on /global/scratch"+'\n')
f.write('\n')
f.write("echo \"TMPDIR is $TMPDIR\""+'\n')
f.write("export TMPDIR4=$TMPDIR"+'\n')
f.write('\n')
f.write("#Copy your input files from the original directory to the scrach directory"+'\n')
f.write("#cp $PBS_O_WORKDIR/$INPUT_FILE.mpi ."+'\n')
f.write("#cp $PBS_O_WORKDIR/$INPUT_FILE.geom ."+'\n')
f.write('\n')
f.write("#Add molpro directory to the path"+'\n')
f.write("#GAS note that it now depends on GA shared library which must be added to the path"+'\n')
f.write('\n')
f.write("module load intel"+'\n')
f.write("module load intel/ompi/1.6.1"+'\n')
f.write('\n')
f.write("export PATH=$PATH:/home/abrown/molpro-12.1-ga/molprop_2012_1_Linux_x86_64_i8/bin"+'\n')
f.write("export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/global/software/ga-5.2-intel-64/lib"+'\n')
f.write('\n')
f.write("#Run molpro in parallel"+'\n')
f.write("# GAS -S ga is needed to tell it is not shared file; number of cores etc."+'\n')
f.write("# should be taken automatically from Torque by OpenMPI's mpiexec."+'\n')
f.write("# -m should control the memory in 8byte words: for pmem 1gb, 8procs it would be about 1gwords?"+'\n')
f.write('\n')
f.write("export ARMCI_DEFAULT_SHMMAX=1800"+'\n')

for i in range(nofk):
#w = coord[i][j]
    f.write(" "+"molpro -v -m 5000m -S ga"+" "+"input_"+str(i)+".mpi"+'\n')
    #f.write(" "+"rm *.pbs.* *xml* input*out* "+'\n')
    f.write(" "+"rm *.pbs.* "+'\n')
#f.write("basis=avtz;"+'\n')
f.write('\n')
f.write("#Copy any output files back to home directory"+'\n')
f.write("#gzip *"+'\n')
f.write("#cp *.gz $PBS_O_WORKDIR"+'\n')
f.write('\n')
f.write("#Remove directories from scratch directory"+'\n')
f.write("##/bin/rm -R $SCRATCHDR"+'\n')
f.write("# GAS $TMPDIR would be removed automatically by Torque"+'\n')
f.write("# so the above isnt needed?"+'\n')
f.write(""+'\n')
f.write("#End of building Molpro job creation and submission file"+'\n')
#######################Modification being done    
