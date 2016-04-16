c#******************************************************
c#* Copyright (C) 2016 Ekadashi Pradhan
c#*
c#******************************************************
	program exchange_rd

	implicit none
	double precision a(60,1),b(1,60)
	integer i,j

	open(11,file='rd_new')
	open(12,file='rd_exchange')


	do i=1,60
	read(11,*)(a(i,1))
	end do

	do i=1,60
	 b(1,i)=a(i,1)
	end do

	do i=1,1
	write(12,91)(b(i,j),j=1,60)
	end do

91	format(60(f32.15,3x))

	end 
