c******************************************************
c* Copyright (C) 2016 Ekadashi Pradhan
c*
c******************************************************

      program gencoord
      implicit none
cccccc
cccc
cc
c    ******** modification by me(ekadashi) ********
c
c
	double precision a(100000,7),p,q
	integer i,j,n

c
c
c

ccccccccccccccccccccccccccccccccccccccc

	write(6,*)'no of data='
	read(5,*)n
	
	write(6,*)'cutoff energy='
	read(5,*)q

	p=219475.0d0
	
ccccccccccccccccccccccccccccccccccccccc
c	defining equilibrium coordinates
c	
ccccccccccccccccccccccccccccccccccccc

	open(12,file='energy.inp')
	open(13,file='energy.cut')
	do i=1,n
	read(12,*)(a(i,j),j=1,7)
	if (p*a(i,7).lt.q) then
	write(13,99)(a(i,j),j=1,7)
	endif
	end do

99      format(7(f15.10,1x))

ccccccccccccccccccccccccccccccccccccccc
         end
c
cc
cccc
