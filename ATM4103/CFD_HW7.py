# -*- coding: utf-8 -*-
"""
CFD_HW7

@author: SminYu
"""
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
#%% Inital condition grid

def Initial_grid(alpha):
    dx = 0.02 ; dt = 0.01
    pi_grid = np.zeros((int(3/dt+1),int(3/dx+1)))

    for i in range(int(3/dx)):
        xx = i*dx - 1.5
        pi_grid[0,i] = 1/(1+np.exp(alpha*(abs(xx)-0.15)))
        
    return pi_grid

#%% FTCS

def FTCS(alpha):
    pi_ftcs = Initial_grid(alpha)
    dx = 0.02 ; dt = 0.01
    cc = 1
    rr= cc*dt/dx
    
    for n in range(int(3/dt)):
        
        pi_ftcs[n+1,0] = pi_ftcs[n,0] - (rr/2.) * (pi_ftcs[n,1] - pi_ftcs[n,-2])
        
        for j in range(1, int(3/dx)):
            pi_ftcs[n+1,j] = pi_ftcs[n,j] - (rr/2.) * (pi_ftcs[n,j+1] - pi_ftcs[n,j-1])

        pi_ftcs[n+1,-1] = pi_ftcs[n,-1] - (rr/2.) * (pi_ftcs[n,1] - pi_ftcs[n,-2])

    return pi_ftcs

#%% Upwind

def Upwind(alpha):
    pi_up = Initial_grid(alpha)
    dx = 0.02 ; dt = 0.01
    cc = 1
    rr = cc*dt/dx
    
    for n in range(int(3/dt)):
        for j in range(int(3/dx)+1):
            if (j != 0):
                pi_up[n+1,j] = pi_up[n,j] - rr * (pi_up[n,j] - pi_up[n,j-1])
            else:
                pi_up[n+1,j] = pi_up[n,j] - rr * (pi_up[n,0] - pi_up[n,-2])
        pi_up[n,0] = pi_up[n,-1]

    return pi_up

#%% Lax-Fredrichs

def Lax_F(alpha):
    pi_laxf = Initial_grid(alpha)
    dx = 0.02 ; dt = 0.01
    cc = 1
    rr = cc*dt/dx
    
    for n in range(int(3/dt)):
        pi_laxf[n+1,0] = 0.5*(pi_laxf[n,1] + pi_laxf[n,-2]) - 0.5*rr*(pi_laxf[n,1] - pi_laxf[n,-2])
        
        for j in range(1,int(3/dx)):
            pi_laxf[n+1,j] = 0.5*(pi_laxf[n,j+1] + pi_laxf[n,j-1]) - 0.5*rr*(pi_laxf[n,j+1] - pi_laxf[n,j-1])
            
        pi_laxf[n+1,int(3/dx)]=0.5*(pi_laxf[n,1] + pi_laxf[n,int(3/dx)-1]) - 0.5*rr*(pi_laxf[n,0] - pi_laxf[n,int(3/dx)-1])
        
    return pi_laxf

#%% Lax-Wendroff

def Lax_W(alpha):
    pi_laxw = Initial_grid(alpha)
    dx = 0.02 ; dt = 0.01
    cc = 1
    rr = cc*dt/dx
    
    for n in range(int(3/dt)):
        pi_laxw[n+1,0] = pi_laxw[n,0] - 0.5*rr*(pi_laxw[n,0] - pi_laxw[n,-2]) + 0.5*(rr**2)*(pi_laxw[n,1] - 2*pi_laxw[n,0] + pi_laxw[n,-2])    
        
        for j in range(1,int(3/dx)): 
            pi_laxw[n+1,j] = pi_laxw[n,j] - 0.5*rr*(pi_laxw[n,j+1] - pi_laxw[n,j-1]) + 0.5*(rr**2)*(pi_laxw[n,j+1] - 2*pi_laxw[n,j] + pi_laxw[n,j-1])
                
        pi_laxw[n+1,-1] = pi_laxw[n,-1] + (-0.5*rr*(pi_laxw[n,1] - pi_laxw[n,-2]) + 
                                        0.5*(rr**2)*(pi_laxw[n,1] - 2*pi_laxw[n,-1] + pi_laxw[n,-2]))
                
    return pi_laxw

#%%
def Plotting(scheme_name, pi, alpha):

    plt.figure(figsize=(10,14))
    plt.suptitle(str(scheme_name)+' scheme α=%d' % alpha, fontsize=20)
    dt = 0.01
    for i in range(1,11):
        plt.subplot(5, 2, i)
        plt.plot(pi[int(30*i),:])
        plt.xlim(0,151)
        plt.ylim(-0.2,1.1)
        plt.xticks([0,25,50,75,100,125,150], [-1.5,-1,-0.5,0,0.5,1.0,1.5])
        plt.text(120,0.9,('t = %5.3f' % (30*i*dt)))
    plt.show()   

    return

#%% Initial condition grid plotting

for alpha_value in [15,80]:
    plt.figure(figsize=(8,6))
    plt.plot(Initial_grid(alpha_value)[0,:])
    plt.xlim(0,151)
    plt.ylim(-0.2,1.1)
    plt.xticks([0,25,50,75,100,125,150], [-1.5,-1,-0.5,0,0.5,1.0,1.5])
    plt.xlabel('X') ; plt.ylabel('Φ')
    plt.title('Initial condition α=%d' % alpha_value)
    plt.show()
   
#%% Plotting for alpha = 15 & 80
for alpha_value in [15,80]:
    Plotting('FTCS', FTCS(alpha_value), alpha_value)
    Plotting('Upwind', Upwind(alpha_value), alpha_value)
    Plotting('Lax-Fredrichs', Lax_F(alpha_value), alpha_value)
    Plotting('Lax-Wendroff', Lax_W(alpha_value), alpha_value)
    
#%% Maximum comparison
plt.figure(figsize=(8,6))
for alpha_value in [15,80]:
    plt.plot(list(map(max, Upwind(alpha_value)))/list(map(max, Upwind(alpha_value)))[0], label ='Upwind'+str(alpha_value))
    plt.plot(list(map(max, Lax_F(alpha_value)))/list(map(max, Lax_F(alpha_value)))[0], label = 'Lax-Friedrichs'+str(alpha_value))
    plt.plot(list(map(max, Lax_W(alpha_value)))/list(map(max, Lax_F(alpha_value)))[0], label = 'Lax-Wendroff'+str(alpha_value))
plt.xticks([0,50,100,150,200,250,300], [0,0.5,1.0,1.5,2.0,2.5,3.0])
plt.xlabel('t') ; plt.ylabel('Relative maximum Φ value')
plt.legend()
plt.title('Realative Amplitude Comparison')
plt.show()
