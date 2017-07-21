c******************************************************
c* Copyright (C) 2016 Ekadashi Pradhan
c*
c******************************************************

      program gen_input

c#######this code generates geometry files later used in 
c       random data calculation using Molpro
c       ONO and HON are converted back to degrees
c       torsional angle is also returned back to degrees

	implicit none
        double precision a(10000,7),p,pi
        integer i,n,j,k
        double precision r1,r2,r3,Q1,Q2,phi


	write(6,*)'no of data='
	read(5,*)n
        open(12,file='train.inp')
	
	pi=acos(-1.0d0)
	p=180.0/pi
	write(6,*)'p=',p
        do i=1,n
        read(12,*)(a(i,j),j=1,7)

c       Each file contains 500 geometry
ccccccccccccccccccccccccccccccccccccccccc
	if (i.le.500) then
         open(15,file='file1.geom')
         write(15,91)'R1(',i,')=',a(i,1)
     +   ,'R2(',i,')=',a(i,2)
     +   ,'R3(',i,')=',a(i,3)
     +   ,'R4(',i,')=',p*acos(a(i,4))
     +   ,'R5(',i,')=',p*acos(a(i,5))
     +   ,'R6(',i,')=',p*a(i,6)
91      format(3(A,i4,A,f8.5,',')
     +   ,2(A,i4,A,f8.3,',')
     +   ,(A,i4,A,f8.3))
	endif
ccccccccccccccccccccccccccccccccccccccccc
	if(i.gt.500) then
	 if(i.le.1000) then
	 k=i-500
        open(16,file='file2.geom')
         write(16,92)'R1(',k,')=',a(i,1)
     +   ,'R2(',k,')=',a(i,2)
     +   ,'R3(',k,')=',a(i,3)
     +   ,'R4(',k,')=',p*acos(a(i,4))
     +   ,'R5(',k,')=',p*acos(a(i,5))
     +   ,'R6(',k,')=',p*a(i,6)
92      format(3(A,i4,A,f8.5,',')
     +   ,2(A,i4,A,f8.3,',')
     +   ,(A,i4,A,f8.3))
	  endif
	 endif
cccccccccccccccccccccccccccccccccccccccccc
	if(i.gt.1000) then
	 if(i.le.1500) then
	 k=i-1000
        open(17,file='file3.geom')
         write(17,93)'R1(',k,')=',a(i,1)
     +   ,'R2(',k,')=',a(i,2)
     +   ,'R3(',k,')=',a(i,3)
     +   ,'R4(',k,')=',p*acos(a(i,4))
     +   ,'R5(',k,')=',p*acos(a(i,5))
     +   ,'R6(',k,')=',p*a(i,6)
93      format(3(A,i4,A,f8.5,',')
     +   ,2(A,i4,A,f8.3,',')
     +   ,(A,i4,A,f8.3))
	  endif
	 endif
cccccccccccccccccccccccccccccccccccccccccc
	if(i.gt.1500) then
	 if(i.le.2000) then
	 k=i-1500
        open(18,file='file4.geom')
         write(18,94)'R1(',k,')=',a(i,1)
     +   ,'R2(',k,')=',a(i,2)
     +   ,'R3(',k,')=',a(i,3)
     +   ,'R4(',k,')=',p*acos(a(i,4))
     +   ,'R5(',k,')=',p*acos(a(i,5))
     +   ,'R6(',k,')=',p*a(i,6)
94      format(3(A,i4,A,f8.5,',')
     +   ,2(A,i4,A,f8.3,',')
     +   ,(A,i4,A,f8.3))
	  endif
	 endif
cccccccccccccccccccccccccccccccccccccccccc
	if(i.gt.2000) then
	 if(i.le.2500) then
	 k=i-2000
        open(19,file='file5.geom')
         write(19,95)'R1(',k,')=',a(i,1)
     +   ,'R2(',k,')=',a(i,2)
     +   ,'R3(',k,')=',a(i,3)
     +   ,'R4(',k,')=',p*acos(a(i,4))
     +   ,'R5(',k,')=',p*acos(a(i,5))
     +   ,'R6(',k,')=',p*a(i,6)
95      format(3(A,i4,A,f8.5,',')
     +   ,2(A,i4,A,f8.3,',')
     +   ,(A,i4,A,f8.3))
	  endif
	 endif
cccccccccccccccccccccccccccccccccccccccccc

        end do


        end program
