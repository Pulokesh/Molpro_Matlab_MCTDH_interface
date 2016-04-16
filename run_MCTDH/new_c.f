c#******************************************************
c#* Copyright (C) 2016 Ekadashi Pradhan
c#*
c#******************************************************

	program new_c

	implicit none

	double precision c,cNew,E_rng,E_mn,a(2,7)
	integer i,j

	open (11,file='HFCO.c')
	read(11,*)c
	open(12,file='c_new')
	open(13,file='mn_rng')
	do i=1,2
        read(13,*)(a(i,j),j=1,7)
        end do

	E_mn  = a(1,7)
	E_rng = a(2,7)
	
	cNew = c*E_rng*0.50d0+E_mn+E_rng*0.50d0

	write(12,99)cNew

99	format(f15.9)

	end
