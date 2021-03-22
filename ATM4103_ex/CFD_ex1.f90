program cfd_ex1
    implicit none
    
    real :: h, t, stop_point
    real :: exact_y, diff_y
    real, dimension(:), allocatable :: y
    integer :: nt, i

    stop_point = 10
    t = 0
    nt = 50
    h = stop_point/real(nt)

    allocate(y(nt+1))
    y(1) = 0

    do i=1, nt
        y(i+1) = y(i)+h*(1+y(i))*cos(t)
        t = t+h

        exact_y = -1+exp(sin(t))
        diff_y = y(i+1) - exact_y
        
        print *, t, y(i+1), exact_y, diff_y
    end do
    
end program cfd_ex1