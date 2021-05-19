# -*- coding: utf-8 -*-
"""
CFD_HW4
@author: SminYu
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
%matplotlib qt5
#%% Initalization
kappa = 1.0

dt = 0.001 ; dx = 0.01
len_t = 2.0 ; len_x = 1.0
rr = kappa * dt / dx**2

xx = int(len_x/dx) ; tt = int(len_t/dt)  


    
#%% FTCS method
# Boundary and Initial conditions
grid = np.zeros((xx+1, tt+1))

for j in range(int(xx/2)+1):
    grid[j,0] = 2*j*dx
    grid[xx-j,0] = 2*(j*dx)
    
for n in range(tt):
    for j in range(1,xx):
        grid[j,n+1] = grid[j,n] + rr * (grid[j-1,n] - 2*grid[j,n] + grid[j+1,n])

    
#%% BTCS method
# Boundary and Initial conditions
grid2 = np.zeros((xx+1, tt+1))

for j in range(int(xx/2)+1):
    grid2[j,0] = 2*j*dx
    grid2[xx-j,0] = 2*(j*dx)

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


#%% plot

fig = plt.figure(figsize=(8,6))
ax = plt.axes(xlim=(0, 1), ylim=(0, 1))
line, = ax.plot([], [])

def update(i):
    line.set_data(np.linspace(0, 1, int(1./dx)+1), grid2[:,i])
    plt.title('t= %5.3F' %(i*dt))
    return line,
    
ani = FuncAnimation(fig, update,  frames=200, interval=50)
HTML(ani.to_html5_video())
        