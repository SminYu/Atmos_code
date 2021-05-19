# -*- coding: utf-8 -*-
"""
CFD_HW4
@author: SminYu
"""
import numpy as np
import matplotlib.pyplot as plt
#%% FTCS Initalization
kappa = 1.0

dt = 0.001 ; dx = 0.1
len_t = 2.0 ; len_x = 1.0
rr = kappa * dt / dx**2

xx = int(len_x/dx) ; tt = int(len_t/dt)  

# Boundary and Initial conditions
grid = np.zeros((xx+1, tt+1))

for j in range(int(xx/2)+1):
    grid[j,0] = 2*j*dx
    grid[xx-j,0] = 2*(j*dx)
    
#%% FTCS method
for n in range(tt):
    for j in range(1,xx):
        grid[j,n+1] = grid[j,n] + rr * (grid[j-1,n] - 2*grid[j,n] + grid[j+1,n])
        
#%% Initial plot
plt.plot(grid[:,0])
plt.xlabel('x') ; plt.ylabel('T')
plt.xticks([0.,0.25*xx,0.5*xx,0.75*xx,xx],[0.0,0.25,0.5,0.75,1.0])
plt.title('t = 0')
plt.show()
        
#%% Plot
plt.figure(figsize=(12,10))
for i,j in zip([.5,1.,1.5,2.], [1,2,3,4]):
    plot_time = i
    plt.subplot(2,2,j)
    plt.plot(grid[:,int(plot_time/2.0*tt)])
    plt.xlabel('x') ; plt.ylabel('T')
    plt.xticks([0.,0.25*xx,0.5*xx,0.75*xx,xx],[0.0,0.25,0.5,0.75,1.0])
    plt.title('t = %3.2F with dt = %4.3F, dx= %4.3F' % (plot_time, dt, dx))
plt.show()

#%% BTCS Initalization 
dt = 0.01 ; dx = 0.1
len_t = 2.0 ; len_x = 1.0
rr = kappa * dt / dx**2

xx = int(len_x/dx) ; tt = int(len_t/dt)  

#Boundary and Initial conditions
grid2 = np.zeros((xx+1, tt+1))

for j in range(int(xx/2)+1):
    grid2[j,0] = 2*j*dx
    grid2[xx-j,0] = 2*(j*dx)
    
#%% BTCS method
mat_A = np.zeros((xx-1,xx-1))

for n in range(1,tt+1):
    for i in range(xx-1):
        mat_A[i,i] = 1+2*rr #d = 1+2r
    for i in range(xx-2):
        mat_A[i,i+1] = -rr #a = -r
        mat_A[i+1,i] = -rr #b = -r
      
    mat_r = np.zeros(xx-1)
    for i in range(xx-1):
        mat_r[i] = grid2[i+1,n-1]

    # Thomas algorithm
    mat_A[0,1] = mat_A[0,1]/mat_A[0,0] #a1 = a1/d1
    mat_r[0] = mat_r[0]/mat_A[0,0] #r1 = r1/d1
    
    for j in range(1,xx-2):
        mat_A[j,j+1] = mat_A[j,j+1]/(mat_A[j,j] - mat_A[j,j-1]*mat_A[j-1,j])
        #ai = ai / di - bi*ai-1
    for j in range(1,xx-1):    
        mat_r[j] = (mat_r[j] - mat_A[j,j-1]*mat_r[j-1]) / (mat_A[j,j] - mat_A[j,j-1]*mat_A[j-1,j])
        #ri = (ri - bi*ri-1)/(di - bi*ai-1)     
                                    
    grid2[-2,n] = mat_r[-1]
    #xn = rn
    
    for i in range(1,xx-1):
        grid2[-i-2,n] = mat_r[-i-1] - mat_A[-i-1,-i]*grid2[-i-1,n]
        #xi = ri - ai*xi+1  from n-1 to 1

#%% Plot
plt.figure(figsize=(12,10))
for i,j in zip([0.5,1.0,1.5,2.0], [1,2,3,4]):
    plot_time = i
    plt.subplot(2,2,j)
    plt.plot(grid2[:,int(plot_time/2.0*tt)])
    plt.xlabel('x') ; plt.ylabel('T')
    plt.xticks([0.,0.25*xx,0.5*xx,0.75*xx,xx],[0.0,0.25,0.5,0.75,1.0])
    plt.title('t = %3.2F with dt=%4.3F, dx=%4.3F' % (plot_time, dt, dx))
plt.show()

#%% comparison plot
plt.figure(figsize=(12,10))
for i,j in zip([0.5,1.0,1.5,2.0], [1,2,3,4]):
    plot_time = i
    plt.subplot(2,2,j)
    plt.plot(grid2[:,int(plot_time/2.0*tt)], label='BTCS')
    plt.plot(grid[:,int(plot_time/2.0*tt)], label='FTCS')
    plt.xlabel('x') ; plt.ylabel('T')
    plt.xticks([0.,0.25*xx,0.5*xx,0.75*xx,xx],[0.0,0.25,0.5,0.75,1.0])
    plt.title('t = %3.2F with dt = %4.3F, dx= %4.3F' % (plot_time, dt, dx))
    plt.legend()
plt.show()