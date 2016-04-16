#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************

import glob   
import math
import sys
import os

path = '/home/ekadashi/HFCO/HFCO_paper_review/30k_cut_PES/Random_1D/100N/*.inp'   
files=glob.glob(path)   
N = len(files)
print N
#sys.exit(0)
fi = open("submit_tmpl.pbs","r")
fsub = open("sim_submit.sh", "w")
fa = fi.readlines()
nfa = len(fa)
fi.close()
for file in files:
    print file
    af = file.split('/')
    print af[8]
    f = open("submit_%s.pbs" %af[8], "w")
    for j in range(0,nfa):
        f.write(fa[j])
    f.write("\n")
    f.write("mctdh84 -mnd %s" %af[8])
    fsub.write("qsub submit_%s.pbs \n" %af[8])
    f.close()    
fsub.close()

