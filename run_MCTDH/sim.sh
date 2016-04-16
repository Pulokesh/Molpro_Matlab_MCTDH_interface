c#******************************************************
c#* Copyright (C) 2016 Ekadashi Pradhan
c#*
c#******************************************************
module load compiler/intel/13.0.1
module load application/python/2.7.3
cp train analysis.inp
ifort -o analys analysis.f
./analys
cp analysis.out mn_rng
ifort -o cnew new_c.f
./cnew
ifort -o iwnew new_IW.f
./iwnew
ifort -o rdnew new_rd.f
./rdnew
ifort -o exc exchange_rd.f
./exc
cp HFCO.LW LW
cp HFCO.b b
cp c_new c
cp IW_new IW
cp rd_exchange rd
python new_genop.py
