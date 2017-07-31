c******************************************************
c* Copyright (C) 2016 Ekadashi Pradhan
c*
c******************************************************

	program ranpts

c       this is for generating random sample points
c       based on sum-over 1D cut PES of HONO
c       range.inp is the input file and trainset is the output
c       where randomly selected data points are stored

        double precision max(10),min(10),d_rand
        double precision Ecut,count,target,countrnd,p
        integer i,n, seed(2), time(8)
	double precision r1,r2,r3,Q1,Q2,phi,v

	open(12,file='range.inp')
	open(14,file='trainset')

c       reads range.inp file where grid ranges are defined
        do i=1,6
        read(12,*)max(i),min(i)
        end do

	write(6,*)'Input cut of energy in cm-1 ?'
	read(5,*)p

        Ecut=p/219475.0d0

        write(6,*)'cut of energy=',p,'cm-1',Ecut,'hartree'
	write(6,*)'no of points u want'
	read(5,*)target

c       Large number of random number (maximum) passed through filter
        n=950000000

        count=0.0d0
	countrnd=0.0d0

ccccc   Random seeds are generated based on timer
	call DATE_AND_TIME(values=time)
	seed(1)=time(4)*(360000*time(5)+6000*time(6)+100*time(7)+time(8))
        print*,'seed=',seed(1)

        call RANDOM_SEED(PUT=seed)
ccccc
	do i=1,n
c	This is just to chek how many random numbers are actually used
	if (((i/1000)*1000).eq.i) then
        write(6,*) d_rand
	endif

c       In the following, each of these 6 coordinates are initiated with
c       a separate random number
        call random_number(d_rand)
        r1=(max(1)-min(1))*d_rand+min(1)
        call random_number(d_rand)
        r2=(max(2)-min(2))*d_rand+min(2)
        call random_number(d_rand)
        r3=(max(3)-min(3))*d_rand+min(3)
        call random_number(d_rand)
        Q1=(max(4)-min(4))*d_rand+min(4)
        call random_number(d_rand)
        Q2=(max(5)-min(5))*d_rand+min(5)
        call random_number(d_rand)
        phi=(max(6)-min(6))*d_rand+min(6)
c	write(6,*)i
c       Finally, calls sum-over 1D cut PES
        call hono(r1,r2,r3,Q1,Q2,phi,v)

        if (v.lt.Ecut) then
c       stops when target total random number is achieved.
        if (count.eq.target) then
        go to 100
        endif

c       Energy filter is now utilized for sampling
        call random_number(d_rand)
         if (((Ecut-v)/Ecut).gt.d_rand) then
         write(14,93)r1,r2,r3,Q1,Q2,phi,v
93      format(7(f15.10,1x))

         count=count+1

         endif
        endif

	countrnd=countrnd+1

        end do

100     continue
	write(6,*)'no of rnd=',countrnd

        end program

cccccccccccccccccccccccccccccccccccccccccccccccccccc
      subroutine hono(r1,r2,r3,o1,o2,phi,v)
c==================================================
c     r1 distance N=O   r2 distance O-N  r3 distance O-H
c     o1 angle O-N-O    o2 angle H-O-N
c     phi dihedral angle
c
c     *********************************************
c     r1, r2, and r3 are fitted with Morse function
c     cosQ1, cosQ2, and Phi are fitted with fifth or more order polynomial
c
c==================================================
	Implicit none
	
	double precision x(6),Xe(3),De(3),A0(3)
	double precision r1,r2,r3,o1,o2,phi,v
	double precision V_1d,v_str,v_1db,v2_tot
	double precision C(3,10),v_bend
	double precision v_phi,A01,A1,A2,A3,A4
	integer i,j,k

c******************************************************
	x(1) = r1
	x(2) = r2
	x(3) = r3
	x(4) = o1
	x(5) = o2
	x(6) = phi

c******************************************************
	Xe(1) = 2.210949d0 
	Xe(2) = 2.6814843d0
	Xe(3) = 1.82545020d0

c******************************************************
	De(1) = 0.234724d0
	De(2) = 0.0712359d0
	De(3) = 0.177202d0

c******************************************************
	A0(1) = 1.36128d0
	A0(2) = 1.21988d0
	A0(3) = 1.21451d0

c******************************************************
	C(1,1) = 0.0454297d0
	C(1,2) = 0.289274d0
	C(1,3) = 0.579192d0
	C(1,4) = 0.445615d0
	C(1,5) = 0.265011d0

	C(2,1) = 0.00483919d0
	C(2,2) = 0.0470909d0
	C(2,3) = 0.123341d0
	C(2,4) = 0.0478834d0
	C(2,5) = 0.0299907d0
	
	A01 = 0.0103183d0
	A1  = 0.00118698d0
	A2  = -0.0096204d0
	A3  = -0.000340861d0
	A4  = 0.000142621d0
	
c******************************************************
	v_str = 0.0d0
	do i=1,3
	V_1d = De(i)*(1-exp(-1.0d0*A0(i)*(x(i)-Xe(i))))**2
	v_str = V_1d + v_str
	end do
	
	v_phi=0.0d0
	
	v_bend = 0.0d0
	do i=1,2
	k=i+3
	v2_tot = 0.0d0
	do j=1,5
	V_1db = C(i,j)*(x(k))**(j-1)
	v2_tot = V_1db + v2_tot
	end do
	v_bend = v_bend + v2_tot
	end do

	v_phi = A01+A1*cos(x(6))+A2*cos(2*x(6))+A3*cos(3*x(6))
     +  + A4*cos(4*x(6))

	v = v_bend + v_str+v_phi
c	write(6,*)v
	return
	end
	
ccccccccccccccccccccccccccc
ccccccccccccccccccccccccccccccc
cccccccccccccccccccccccccccccccccccc
