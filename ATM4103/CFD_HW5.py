# -*- coding: utf-8 -*-
"""
CFD_HW5

@author: SminYu
"""
import numpy as np
import matplotlib.pyplot as plt

#%% Kappa-value
kappa = 1.0

#%% CTCS
# CTCS Initialization
dt = 0.001 ; dx = 0.1
len_t = 2.0 ; len_x = 1.0
rr = kappa * dt / dx**2

xx = int(len_x/dx) ; tt = int(len_t/dt)  

# Boundary and Initial conditions
T_df = np.zeros((xx+1, tt+1))

for j in range(int(xx/2)+1):
    T_df[j,0] = 2*j*dx
    T_df[xx-j,0] = 2*(j*dx)
    
# CTCS method (Dufort-Frankel method)
for n in range(tt):
    for j in range(1,xx):
        T_df[j,n+1] = (1-2*rr)/(1+2*rr)*T_df[j,n-1] + 2*rr/(1+2*rr)*(T_df[j+1,n]+T_df[j-1,n])
        
# Plot
plt.figure(figsize=(12,10))
for i,j in zip([.5,1.,1.5,2.], [1,2,3,4]):
    plot_time = i
    plt.subplot(2,2,j)
    plt.plot(T_df[:,int(plot_time/2.0*tt)])
    plt.xlabel('x') ; plt.ylabel('T')
    plt.xticks([0.,0.25*xx,0.5*xx,0.75*xx,xx],[0.0,0.25,0.5,0.75,1.0])
    plt.title('t = %3.2F with dt = %4.3F, dx= %4.3F' % (plot_time, dt, dx))
plt.show()        

#%% Initial plot
plt.figure(figsize=(6,5))
plt.plot(T_df[:,0])
plt.xlabel('x') ; plt.ylabel('T')
plt.xticks([0.,0.25*xx,0.5*xx,0.75*xx,xx],[0.0,0.25,0.5,0.75,1.0])
plt.title('t = 0')
plt.show()

#%% RK2
# Initalization 
dt = 0.001 ; dx = 0.1
len_t = 2.0 ; len_x = 1.0
rr = kappa * dt / dx**2

xx = int(len_x/dx) ; tt = int(len_t/dt)  

#Boundary and Initial conditions
T_rk = np.zeros((xx+1, tt+1))
T_star = np.zeros(xx+1)
             
for j in range(int(xx/2)+1):
    T_rk[j,0] = 2*j*dx
    T_rk[xx-j,0] = 2*(j*dx)
    
# RK2 method
for n in range(tt):
    for j in range(1,xx):
        T_star[j] = T_rk[j,n] + rr/2. * (T_rk[j+1,n] - 2*T_rk[j,n] + T_rk[j-1,n])
    for j in range(1,xx):
        T_rk[j,n+1] = T_rk[j,n] + rr * (T_star[j+1] - 2*T_star[j] + T_star[j-1])
                                          
# Plot
plt.figure(figsize=(12,10))
for i,j in zip([0.5,1.0,1.5,2.0], [1,2,3,4]):
    plot_time = i
    plt.subplot(2,2,j)
    plt.plot(T_rk[:,int(plot_time/2.0*tt)])
    plt.xlabel('x') ; plt.ylabel('T')
    plt.xticks([0.,0.25*xx,0.5*xx,0.75*xx,xx],[0.0,0.25,0.5,0.75,1.0])
    plt.title('t = %3.2F with dt=%4.3F, dx=%4.3F' % (plot_time, dt, dx))
plt.show()

#%% comparison plot
plt.figure(figsize=(12,10))
for i,j in zip([0.5,1.0,1.5,2.0], [1,2,3,4]):
    plot_time = i
    plt.subplot(2,2,j)
    plt.plot(T_df[:,int(plot_time/2.0*tt)], label='CTCS')
    plt.plot(T_rk[:,int(plot_time/2.0*tt)], label='RK2')
    plt.xlabel('x') ; plt.ylabel('T')
    plt.xticks([0.,0.25*xx,0.5*xx,0.75*xx,xx],[0.0,0.25,0.5,0.75,1.0])
    plt.title('t = %3.2F with dt = %4.3F, dx= %4.3F' % (plot_time, dt, dx))
    plt.legend()
plt.show()

#%% peak comparison
plt.figure(figsize=(8,6))
plt.plot(T_df[int(len_x/dx/2),:100], label='CTCS')
plt.plot(T_rk[int(len_x/dx/2),:100], label='RK2')
plt.title('Peak comparison')
plt.xlabel('n-th cycle') ; plt.ylabel('T')
plt.legend()
plt.show()
