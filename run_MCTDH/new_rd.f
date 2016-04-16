c#******************************************************
c#* Copyright (C) 2016 Ekadashi Pradhan
c#*
c#******************************************************

	program new_rd

	implicit none
	double precision d_1,d_2,d_3,E_rng
	double precision a(60,6),b(60,6),X(2,7)
	integer i,j


	open(11,file='HFCO.IW')
	open(13,file='mn_rng')
	open(12,file='rd_new')

c	E_rng = X(2,7)
	
	write(6,*)'1. did you change E_rng ?'
	write(6,*)'2. dont forget to change input file'

	do i=1,2
	 read(13,*)(X(i,j),j=1,7)
	end do

	E_rng = X(2,7)

	do i=1,60
	 read(11,*)(a(i,j),j=1,6)
	end do

	do i=1,60
	 d_1 = 1.0d0
	  do j=1,6
	   d_2 = 2.0d0*(a(i,j))*(X(1,j))/(X(2,j))+a(i,j)
	   d_3 = exp(d_2*(-1.0d0))
	   d_1 = d_3*d_1
	  end do
	write(12,91)d_1*0.50d0*E_rng
	end do
	write(6,*)d_1,d_2,d_3

91	format(f32.15)

	end
