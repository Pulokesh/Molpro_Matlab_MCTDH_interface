c******************************************************
c* Copyright (C) 2016 Ekadashi Pradhan
c*
c******************************************************
      program analysis

c******************************************************
c       >> To fond maxima and minima of each physical coordinates.
c       >> To find # points above and below equilibrium of each coordinates.
c       >> To find E_max and energy range in train, test and val set.
c       
c    **********************************************
	implicit none
	double precision rmin(7),rmax(7)
	double precision a(50000,7)
        integer i,j,n

c    **********************************************
	open(12,file='analysis.inp')
	open(14,file='analysis.out')

c    **********************************************
	write(6,*)'no of rows='
	read(5,*)n

	do i=1,n
	read(12,*)(a(i,j),j=1,7)
	end do

	do i=1,7
	rmax(i)=a(1,i)
	rmin(i)=a(1,i)
	end do

c    **********************************************
	 do i=1,n
	  do j=1,7
	  if (a(i,j).gt.rmax(j)) then
	  rmax(j)=a(i,j)
	  endif
	  if (a(i,j).lt.rmin(j)) then
	  rmin(j)=a(i,j)
	  endif
	  end do
	 end do

c	*************************************************
	write(14,99)rmin(1),rmin(2),rmin(3),rmin(4),rmin(5),rmin(6),rmin(7)
	write(14,99)rmax(1)-rmin(1),rmax(2)-rmin(2),rmax(3)-rmin(3)
     +  ,rmax(4)-rmin(4),rmax(5)-rmin(5),rmax(6)-rmin(6),rmax(7)-rmin(7)

99	format (7f11.7,x)

	end
