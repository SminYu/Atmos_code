program CFD_HW2
    implicit none

    real, dimension(161) :: t, y_euler, y_lf, y_ab2, y_ab3, y_exact
    real :: l2_euler, l2_lf, l2_ab2, l2_ab3
    integer :: i, step
    real :: h
    real, parameter :: pi = 4.*atan(1.)

    step = 10
    do while (step <= 160)

        !initialization
        y_euler = 0
        y_lf = 0
        y_ab2 = 0
        y_ab3 = 0
        y_exact = 0
        t(1) = 0
        
        h = 3.*pi/real(step)

        ! Euler scheme and exact value
        l2_euler = 0
        do i=1, step
            t(i+1) = t(i) + h
            y_exact(i+1) = exp(t(i+1)/2.) * sin(5.*t(i+1))
            y_euler(i+1) = (1+h) * y_euler(i) + h * exp(t(i)/2.) * (-0.5*sin(5.*t(i)) + 5.*cos(5.*t(i)))
            l2_euler = l2_euler + (y_exact(i+1) - y_euler(i+1))**2.
        end do
        l2_euler = sqrt(l2_euler)/(step+1)

        !First step is Euler scheme for lf and AB methods because they are not self-started.
        y_lf(2) = y_euler(2)
        y_ab2(2) = y_euler(2)
        l2_lf = (y_euler(2) - y_exact(2))**2
        l2_ab2 = (y_ab2(2) - y_exact(2))**2

        do i=2, step
            y_lf(i+1) = y_lf(i-1) + 2*h * (y_lf(i) + exp(t(i)/2.) * (-0.5*sin(5.*t(i)) + 5.*cos(5.*t(i))) )
            l2_lf = l2_lf + (y_exact(i+1) - y_lf(i+1))**2

            y_ab2(i+1) = y_ab2(i) &
                        + h * (1.5 * (y_ab2(i) + exp(t(i)/2.) * (-0.5*sin(5.*t(i)) + 5.*cos(5.*t(i)))) &
                              - 0.5 * (y_ab2(i-1) + exp(t(i-1)/2.) * (-0.5*sin(5.*t(i-1)) + 5.*cos(5.*t(i-1)))) )
            l2_ab2 = l2_ab2 + (y_exact(i+1) - y_ab2(i+1))**2
        end do

        !For AB3 method, I used Euler scheme for the first step and AB2 scheme for the second.
        y_ab3(2) = y_euler(2)
        y_ab3(3) = y_ab2(3)
        l2_ab3 = (y_ab3(2) - y_exact(2))**2 + (y_ab3(3) - y_exact(3))**2

        do i=3, step
            y_ab3(i+1) = y_ab3(i) &
                    + h/12. * (23. * (y_ab3(i) + exp(t(i)/2.) * (-0.5*sin(5.*t(i)) + 5.*cos(5.*t(i)))) &
                              -16. * (y_ab3(i-1) + exp(t(i-1)/2.) * (-0.5*sin(5.*t(i-1)) + 5.*cos(5.*t(i-1)))) &
                              +5.  * (y_ab3(i-2) + exp(t(i-2)/2.) * (-0.5*sin(5.*t(i-2)) + 5.*cos(5.*t(i-2)))) )
            l2_ab3 = l2_ab3 + (y_exact(i+1) - y_ab3(i+1))**2
        end do    

        l2_lf = sqrt(l2_lf)/(step+1)
        l2_ab2 = sqrt(l2_ab2)/(step+1)
        l2_ab3 = sqrt(l2_ab3)/(step+1)
        
        print *, step, l2_euler, l2_lf, l2_ab2, l2_ab3
 
        open(51, file="HW2.csv")
        write(51, '(A,I3)') 'Step ,', step 
        write(51, '(A,A,A,A,A,A,A,A,A,A,A)') 't', ',', 'y_exact', ',', 'y_euler', ',', 'y_lf', ',', 'y_ab2', ',', 'y_ab3'
            
        do i=1, step+1
            write(51, '(999(F21.6,:,","))') t(i), y_exact(i), y_euler(i), y_lf(i), y_ab2(i), y_ab3(i)
        end do

        !Double the step
        step = step * 2

    end do

end program CFD_HW2