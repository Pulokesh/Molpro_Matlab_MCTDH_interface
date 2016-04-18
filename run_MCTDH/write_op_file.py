#******************************************************
#* Copyright (C) 2016 Ekadashi Pradhan
#*
#******************************************************
##

import math
import sys
import os
from numpy import *

filename = "HFCO.op"
file_tmp = "hfco_op_templ"
fa = open(filename, "r+")
fb = open(file_tmp, "r+")
a = fa.readlines()
b = fb.readlines()
fa.close()
fb.close()
Na = len(a)
Nb = len(b)
for i in range(0,Na):
    aa = a[i].split()
    if len(aa) >0 and aa[0] == "PARAMETER-SECTION":
        param_start = i+1
    elif len(aa) >0 and aa[0] == "end-parameter-section":
        param_end = i
    elif len(aa) >0 and aa[0] == "LABELS-SECTION":
        label_start = i+1
    elif len(aa) >0 and aa[0] == "end-labels-section":
        label_end = i
    elif len(aa) >0 and aa[0] == "HAMILTONIAN-SECTION":
        ham_start = i+1
    elif len(aa) >0 and aa[0] == "end-hamiltonian-section":
        ham_end = i

for k in range(0,Nb):
    bb = b[k].split()
    if len(bb) >0 and bb[0] == "OP_DEFINE-SECTION":
        op_def_start = k
    elif len(bb) >0 and bb[0] == "r0" and bb[1] == "=":
        op_def_end = k-1
    elif len(bb) >0 and bb[0] == "LABELS-SECTION":
        op_label_start = k
    elif len(bb) >0 and bb[0] == "q0u0" and bb[1] == "=":
        op_label_end = k-1
    elif len(bb) >0 and bb[0] == "HAMILTONIAN-SECTION":
        op_ham_start = k
    elif len(bb) >0 and bb[0] == "c" and bb[1] == "|" and bb[2] == "1":
        op_ham_end = k-1
    elif len(bb) >0 and bb[0] == "HAMILTONIAN-SECTION_r1i":
        op_1dham_start = k
    elif len(bb) >0  and bb[0] == "end-operator":
        op_1dham_end = k


filename1 = "hfco1.op"
fop = open(filename1, "w")
for j in range(op_def_start,op_def_end+1):
    fop.write(b[j])
for j in range(param_start,param_end+1):
    fop.write(a[j])
fop.write("\n")

for j in range(op_label_start,op_label_end+1):
    fop.write(b[j])
for j in range(label_start,label_end+1):
    fop.write(a[j])
fop.write("\n")

for j in range(op_ham_start,op_ham_end+1):
    fop.write(b[j])
for j in range(ham_start,ham_end+1):
    fop.write(a[j])
fop.write("\n")

for j in range(op_1dham_start,op_1dham_end+1):
    fop.write(b[j])
fop.write("\n")


fop.close()
print "job Done!"









