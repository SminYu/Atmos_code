# -*- coding: utf-8 -*-
"""
CFD HW6

@author: SminYu
"""
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

#%% make an initial grid with the boundary condition
def Initial_grid(len_x, len_y, dx, dy):
    T_grid = np.zeros((int(len_y/dy)+1, int(len_x/dx)+1))
    T_grid[int(0.25*len_x/dx):int(0.75*len_x/dx)+1,0] = 1
    return T_grid

#%% Jacobi method
def Jacobi(len_x, len_y, delta):
    T_old = Initial_grid(len_x,len_y,delta,delta)
    T_new = Initial_grid(len_x,len_y,delta,delta)
    
    iter_num = 0
    esp = 1
    while (esp > 0.01):
        iter_num += 1
        for j in range(1,len(T_old)-1):
            for i in range(1,len(T_old)-1):
                T_new[j,i] = (T_old[j-1,i] + T_old[j+1,i] + T_old[j,i-1] + T_old[j,i+1])/4
                
        esp = sum(sum(abs(T_new - T_old)/delta**2))/(len_x/delta-1)**2
        
        for j in range(1,len(T_old)-1):
            for i in range(1,len(T_old)-1):
                T_old[j,i] = T_new[j,i]
    
    return T_new, iter_num

#%% Gauss-Seidel
def GaussSeidel(len_x, len_y, delta):
    T_old = Initial_grid(len_x,len_y,delta,delta)
    T_new = Initial_grid(len_x,len_y,delta,delta)
    
    iter_num = 0
    esp = 1
    while (esp > 0.01):
        iter_num += 1
        esp_temp = 0
        for j in range(1,len(T_old)-1):  
            for i in range(1,len(T_old)-1):
                T_new[j,i] = (T_old[j-1,i] + T_old[j+1,i] + T_old[j,i-1] + T_old[j,i+1])/4
                esp_temp += abs(T_old[j,i] - T_new[j,i])/delta**2/(len_x/delta-1)**2
                T_old[j,i] = T_new[j,i]
        esp = esp_temp
        
    return T_new, iter_num
                  
#%% SOR method
def SOR(len_x, len_y, delta, omega):
    T_old = Initial_grid(2,2,delta,delta)
    T_new = Initial_grid(2,2,delta,delta)
    
    iter_num = 0
    esp = 1

    while (esp > 0.01):
        esp = 0
        iter_num += 1
        for j in range(1,len(T_old)-1):
            for i in range(1,len(T_old)-1):
                T_gs = (T_old[j-1,i] + T_old[j+1,i] + T_old[j,i-1] + T_old[j,i+1])/4
                T_new[j,i] = (1-omega) * T_old[j,i] + omega * T_gs
                esp += abs(T_new[j,i] - T_old[j,i])/delta**2/(len(T_old)-1)**2
                T_old[j,i] = T_new[j,i]
    
    return T_new, iter_num

#%% plotting function
def plotting(T_grid, iter_num, delta, func_name):
    plt.figure(figsize=(8,6))
    plt.contourf(T_grid)
    plt.colorbar()
    plt.xlabel('x') ; plt.ylabel('y')
    plt.xticks([0,0.5/delta,1/delta,1.5/delta,2/delta],[0,0.5,1.0,1.5,2.0])
    plt.yticks([0,0.5/delta,1/delta,1.5/delta,2/delta],[0,0.5,1.0,1.5,2.0])
    plt.title(func_name+' method, delta = 1/%d, Iteration = %d'%(1/delta, iter_num))
    plt.show()
    return

#%% SOR method optimization (get the optimal omega)
for delta in [1/20, 1/40]:
    print(delta)
    iter_opti = np.zeros(9)
       
    for ohm in range(9):
        omega = 1.1 + ohm * 0.1
        _, iter_opti[ohm] = SOR(2,2,delta,omega)
        print('omega = %2.1F, iteration = %d'%(omega, iter_opti[ohm]))
        
    plt.figure(figsize=(8,6))
    plt.plot(iter_opti)
    plt.xticks([0,2,4,6,8],[1.1,1.3,1.5,1.7,1.9])
    plt.xlim(0,8)
    plt.xlabel('ω') ; plt.ylabel('Iteration')
    plt.title('delta = 1/%d'%(1/delta))
    plt.show()
    
#%% Calculation and plotting for Jacobi method and G-S method
for i in [20,40]:
    T_j, iter_j = Jacobi(2,2,1/i)
    plotting(T_j, iter_j, 1/i, Jacobi.__name__)

    T_gs, iter_gs = GaussSeidel(2,2,1/i)
    plotting(T_gs, iter_gs, 1/i, GaussSeidel.__name__)
    
    T_sor, iter_sor = SOR(2,2,1/i,1.9) #The optimal omega is 1.9
    plotting(T_sor, iter_sor, 1/i, SOR.__name__) 
    
    
#%%
'''
animation (additional)

from matplotlib.animation import ArtistAnimation
%matplotlib qt5

fig = plt.figure(figsize=(10,8))
ims = []
delta = 1/20
omega = 1.9
len_x = 2
    
T_old = Initial_grid(2,2,delta,delta)
T_new = Initial_grid(2,2,delta,delta)
    
iter_num = 0
esp = 1

while (esp > 0.1):
    iter_num += 1
    esp_temp = 0
    for j in range(1,len(T_old)-1):  
        for i in range(1,len(T_old)-1):
            T_new[j,i] = (T_old[j-1,i] + T_old[j+1,i] + T_old[j,i-1] + T_old[j,i+1])/4
            esp_temp += abs(T_old[j,i] - T_new[j,i])/delta**2/(len_x/delta-1)**2
            T_old[j,i] = T_new[j,i]
    esp = esp_temp
                
    cont = plt.contourf(T_new, vmax=1, vmin=0)
    ims.append(cont.collections)
    
cbar = plt.colorbar(cont)
cbar.set_clim(0,1)
    
plt.xticks([0,0.5/delta,1/delta,1.5/delta,2/delta],[0,0.5,1.0,1.5,2.0])
plt.yticks([0,0.5/delta,1/delta,1.5/delta,2/delta],[0,0.5,1.0,1.5,2.0])

anim = ArtistAnimation(fig, ims, interval=5)

'''

