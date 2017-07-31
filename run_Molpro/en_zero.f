c******************************************************
c* Copyright (C) 2016 Ekadashi Pradhan
c*
c******************************************************

        program en_zero

	double precision a(10000,9),p1,p2,p
	integer i,j,n

	write(6,*)'no of rows='
	read(5,*)n
	open(12,file='energy.inp')
	open(13,file='energy.out')

c	the equilibrium energy ----------
	p = -205.5325070d0
	pi=acos(-1.0d0)
	p1=pi/180.0d0

	do i=1,n
	read(12,*)(a(i,j),j=1,9)
	write(13,99)a(i,1),a(i,2),a(i,3)
     +  ,cos(a(i,4)*p1),cos(a(i,5)*p1),p1*a(i,6)
     +  ,a(i,8)-p
	end do

c99	format(3f10.6,1x)
99	format(7f12.7,1x)
	end
