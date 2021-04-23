PROGRAM AB2
    IMPLICIT NONE

    INTEGER, PARAMETER :: nt=10
    REAL, DIMENSION(nt+1) :: y_guess, y_exact, y_diff
    INTEGER :: i
    REAL :: h, t

    !initialization
    y_exact=0
    y_guess=0
    y_guess(1) = 1
    y_exact(1) = 1
    h=1./nt
    t=0
    
    !take first step with forward scheme
    y_guess(2) = (1-h) * y_guess(1)
    t=1*h
    y_exact(2)=exp(-t)
    y_diff(2)=y_guess(2)-y_exact(2)
	 
    !march with AB2
    do i = 2, nt
        y_guess(i+1) =(1-1.5*h)*y_guess(i)+0.5*h*y_guess(i-1)

        !compute t
        t=i*h
        !compute exact solution
        y_exact(i+1)=exp(-t)

        !compute difference between y_guess and y_exact
        y_diff(i+1)=y_guess(i+1)-y_exact(i+1)   
    end do
	
	!print result as CSV foramt
    !open(51, file="nt_10.csv")
    !write(51, '(A,A,A,A,A,A,A)') 't', ',', 'y_guess', ',', 'y_exact', ',', 'y_diff'
    do i = 1, nt+1
        t=(i-1)*h
        write(*,'(999(F21.6,:,","))') t, y_guess(i), y_exact(i), y_diff(i)
    end do
	
END PROGRAM