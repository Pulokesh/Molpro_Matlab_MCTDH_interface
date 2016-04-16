c#******************************************************
c#* Copyright (C) 2016 Ekadashi Pradhan
c#*
c#******************************************************

	program new_IW

	implicit none
	double precision r1_rng,r2_rng,r3_rng
	double precision Q1_rng,Q2_rng,phi_rng
	double precision a(60,6),b(60,6),c(2,7)
	integer i,j


	open(11,file='HFCO.IW')
	open(12,file='IW_new')
	open(13,file='mn_rng')

	do i=1,2
	read(13,*)(c(i,j),j=1,7)
	end do

	r1_rng = c(2,1)
	r2_rng = c(2,2)
	r3_rng = c(2,3)
	Q1_rng = c(2,4)
	Q2_rng = c(2,5)
	phi_rng= c(2,6)

	write(6,*)'reminder: change NN'
	write(6,*)'reminder: change range value'

	do i=1,60
	 read(11,*)(a(i,j),j=1,6)
	end do

	do i=1,60
	 b(i,1) = 2*(a(i,1))/r1_rng
	 b(i,2) = 2*(a(i,2))/r2_rng
	 b(i,3) = 2*(a(i,3))/r3_rng
	 b(i,4) = 2*(a(i,4))/Q1_rng
	 b(i,5) = 2*(a(i,5))/Q2_rng
	 b(i,6) = 2*(a(i,6))/phi_rng
	end do

	do i=1,60
	write(12,91)(b(i,j),j=1,6)
	end do

91	format(6(f19.15,3x))

	end
