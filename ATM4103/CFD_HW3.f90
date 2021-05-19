program CFD_HW3
    implicit none
    
    integer, parameter :: t_time = 2000
    real :: h, x, y, z, t
    real :: k1, l1, m1, k2, l2, m2, k3, l3, m3, k4, l4, m4
    real, dimension(t_time+1) :: li_t, li_x1, li_y1, li_z1, li_x2, li_y2, li_z2
    integer :: i

! Initiation
    h = 20./real(t_time)
    li_t(1) = 0.

    li_x1(1) = 5.0
    li_y1(1) = 5.0
    li_z1(1) = 5.0

    li_x2(1) = 5.001
    li_y2(1) = 5.001
    li_z2(1) = 5.001

! RK2 method
    do i = 1, t_time
        t = li_t(i)
        li_t(i+1) = t+h

        ! start with 5 (x1,y1,z1)
        x = li_x1(i)
        y = li_y1(i)
        z = li_z1(i)

        k1 = k_value(x,y,z)
        l1 = l_value(x,y,z)
        m1 = m_value(x,y,z)

        k2 = k_value(x+h*k1, y+h*l1, z+h*m1)
        l2 = l_value(x+h*k1, y+h*l1, z+h*m1)
        m2 = m_value(x+h*k1, y+h*l1, z+h*m1)

        li_x1(i+1) = x + h*(k1+k2)/2. 
        li_y1(i+1) = y + h*(l1+l2)/2.
        li_z1(i+1) = z + h*(m1+m2)/2.

        ! start with 5.001 (x2,y2,z2)
        x = li_x2(i)
        y = li_y2(i)
        z = li_z2(i)

        k1 = k_value(x,y,z)
        l1 = l_value(x,y,z)
        m1 = m_value(x,y,z)

        k2 = k_value(x+h*k1, y+h*l1, z+h*m1)
        l2 = l_value(x+h*k1, y+h*l1, z+h*m1)
        m2 = m_value(x+h*k1, y+h*l1, z+h*m1)

        li_x2(i+1) = x + h*(k1+k2)/2. 
        li_y2(i+1) = y + h*(l1+l2)/2.
        li_z2(i+1) = z + h*(m1+m2)/2.
           
    end do

    !wrtie to csv file
    open(51, file="HW3_RK2.csv")
    write(51, '(999(A,:,","))') 't', 'x1', 'y1', 'z1', 'x2', 'y2', 'z2'

    do i=1, t_time+1
        write(51, '(999(F21.6,:,","))') li_t(i), li_x1(i), li_y1(i), li_z1(i), &
                                        li_x2(i), li_y2(i), li_z2(i)
    end do

    
! RK4 method
    do i = 1, t_time
        t = li_t(i)
        li_t(i+1) = t+h

        ! start with 5 (x1,y1,z1)
        x = li_x1(i)
        y = li_y1(i)
        z = li_z1(i)

        k1 = k_value(x,y,z)
        l1 = l_value(x,y,z)
        m1 = m_value(x,y,z)

        k2 = k_value(x+h*k1/2., y+h*l1/2., z+h*m1/2.)
        l2 = l_value(x+h*k1/2., y+h*l1/2., z+h*m1/2.)
        m2 = m_value(x+h*k1/2., y+h*l1/2., z+h*m1/2.)

        k3 = k_value(x+h*k2/2., y+h*l2/2., z+h*m2/2.)
        l3 = l_value(x+h*k2/2., y+h*l2/2., z+h*m2/2.)
        m3 = m_value(x+h*k2/2., y+h*l2/2., z+h*m2/2.)

        k4 = k_value(x+h*k3, y+h*l3, z+h*m3)
        l4 = l_value(x+h*k3, y+h*l3, z+h*m3)
        m4 = m_value(x+h*k3, y+h*l3, z+h*m3)

        li_x1(i+1) = x + h*(k1+ 2.*k2 + 2.*k3 + k4)/6. 
        li_y1(i+1) = y + h*(l1+ 2.*l2 + 2.*l3 + l4)/6.
        li_z1(i+1) = z + h*(m1+ 2.*m2 + 2.*m3 + m4)/6.

        ! start with 5.001 (x2,y2,z2)
        x = li_x2(i)
        y = li_y2(i)
        z = li_z2(i)

        k1 = k_value(x,y,z)
        l1 = l_value(x,y,z)
        m1 = m_value(x,y,z)

        k2 = k_value(x+h*k1/2., y+h*l1/2., z+h*m1/2.)
        l2 = l_value(x+h*k1/2., y+h*l1/2., z+h*m1/2.)
        m2 = m_value(x+h*k1/2., y+h*l1/2., z+h*m1/2.)

        k3 = k_value(x+h*k2/2., y+h*l2/2., z+h*m2/2.)
        l3 = l_value(x+h*k2/2., y+h*l2/2., z+h*m2/2.)
        m3 = m_value(x+h*k2/2., y+h*l2/2., z+h*m2/2.)

        k4 = k_value(x+h*k3, y+h*l3, z+h*m3)
        l4 = l_value(x+h*k3, y+h*l3, z+h*m3)
        m4 = m_value(x+h*k3, y+h*l3, z+h*m3)

        li_x2(i+1) = x + h*(k1+ 2.*k2 + 2.*k3 + k4)/6. 
        li_y2(i+1) = y + h*(l1+ 2.*l2 + 2.*l3 + l4)/6.
        li_z2(i+1) = z + h*(m1+ 2.*m2 + 2.*m3 + m4)/6.
           
    end do

    !wrtie to csv file
    open(52, file="HW3_RK4.csv")
    write(52, '(999(A,:,","))') 't', 'x1', 'y1', 'z1', 'x2', 'y2', 'z2'

    do i=1, t_time+1
        write(52, '(999(F21.6,:,","))') li_t(i), li_x1(i), li_y1(i), li_z1(i), &
                                        li_x2(i), li_y2(i), li_z2(i)
    end do

contains

function k_value(xx,yy,zz)
    real :: xx,yy,zz
    real :: k_value
    k_value = 10.*(yy-xx)
    return
end function k_value

function l_value(xx,yy,zz)
    real :: xx,yy,zz
    real :: l_value
    l_value = 28.*xx - yy - xx*zz
    return
end function l_value

function m_value(xx,yy,zz)
    real :: xx,yy,zz
    real :: m_value
    m_value = xx*yy - 8.*zz/3.
    return
end function m_value

end program CFD_HW3 
