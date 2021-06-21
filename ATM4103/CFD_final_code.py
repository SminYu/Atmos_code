# -*- coding: utf-8 -*-
"""
CFD Final

@author: SminYu
"""
import numpy as np
import matplotlib.pyplot as plt

#%% Initialization
def Initial_grid(lambda_val):
    nx = 301 ; ny = 301

    uu = np.zeros([nt,nx,ny])
    vv = np.zeros([nt,nx,ny])
    hh = np.zeros([nt,nx,ny])
    
    for i in range(nx):
        xx = -100. + i * dx
        hh[0,i,:] = -lambda_val * np.arctan(10.*xx)
    
    return uu, vv, hh

#%% Grid set
nx = 301 ; ny = 301
dx = 200/(nx-1) ; dy = 200/(nx-1)
dt = 0.05 ; nt = 301

#%%FTCS method
def FTCS(g_acc, ff, lambda_input, H_val):
    uu,vv,hh = Initial_grid(lambda_input)
    
    for n in range(nt-1):
        for ii in range(1,nx):
            # if statement for Neumann boundary condition
            ip = ii+1 if ii < nx-1 else ii
            im = ii-1 if ii > 0 else ii  
            
            for jj in range(1,ny):
                jp = jj+1 if jj < ny-1 else jj
                jm = jj-1 if jj > 0 else jj
            
                uu[n+1,ii,jj] = uu[n,ii,jj] - (g_acc*dt/2./dx) * (hh[n,ip,jj] - hh[n,im,jj]) + ff*dt*vv[n,ii,jj]
                vv[n+1,ii,jj] = vv[n,ii,jj] - (g_acc*dt/2./dy) * (hh[n,ii,jp] - hh[n,ii,jm]) - ff*dt*uu[n,ii,jj]
                hh[n+1,ii,jj] = hh[n,ii,jj] - H_val*dt * ((uu[n,ip,jj] - uu[n,im,jj])/2/dx 
                                                           + (vv[n,ii,jp] - vv[n,ii,jm])/2/dy)
        
    return uu, vv, hh

#%% Leapfrog scheme
def leapfrog(g_acc, ff, lambda_input, H_val):
    uu,vv,hh = Initial_grid(lambda_input)
    
    n = 0
    for ii in range(nx):
        ip = ii+1 if ii < nx-1 else ii
        im = ii-1 if ii > 0 else ii
        
        for jj in range(ny):
            jp = jj+1 if jj < ny-1 else jj
            jm = jj-1 if jj > 0 else jj
            
            uu[n+1,ii,jj] = uu[n,ii,jj] - (g_acc*dt/2./dx) * (hh[n,ip,jj] - hh[n,im,jj]) + ff*dt*vv[n,ii,jj]
            vv[n+1,ii,jj] = vv[n,ii,jj] - (g_acc*dt/2./dy) * (hh[n,ii,jp] - hh[n,ii,jm]) - ff*dt*uu[n,ii,jj]
            hh[n+1,ii,jj] = hh[n,ii,jj] - H_val*dt * ((uu[n,ip,jj] - uu[n,im,jj])/2/dx 
                                                       + (vv[n,ii,jp] - vv[n,ii,jm])/2/dy)
    
    for n in range(1,nt-1):
        for ii in range(nx):
            ip = ii+1 if ii < nx-1 else ii
            im = ii-1 if ii > 0 else ii  
            
            for jj in range(ny):
                jp = jj+1 if jj < ny-1 else jj
                jm = jj-1 if jj > 0 else jj
            
                uu[n+1,ii,jj] = uu[n-1,ii,jj] - (g_acc*dt/dx) * (hh[n,ip,jj] - hh[n,im,jj]) + ff*dt*vv[n,ii,jj]
                vv[n+1,ii,jj] = vv[n-1,ii,jj] - (g_acc*dt/dy) * (hh[n,ii,jp] - hh[n,ii,jm]) - ff*dt*uu[n,ii,jj]
                hh[n+1,ii,jj] = hh[n-1,ii,jj] - H_val*dt * ((uu[n,ip,jj] - uu[n,im,jj])/dx 
                                                             + (vv[n,ii,jp] - vv[n,ii,jm])/dy)
    
    return uu, vv, hh


#%% Computation    
# Without rotational effect (f = 0)
u_ftcs_f0, v_ftcs_f0, h_ftcs_f0 = FTCS(9.8, 0., 1., 10.)
u_lf_f0, v_lf_f0, h_lf_f0 = leapfrog(9.8, 0., 1., 10.)

# default set (g=9.8, f=0.0001, lambda=1, H=10)
u_default, v_default, h_default = leapfrog(9.8, 0.0001, 1., 10.) 

# f variation (f=1, 10, 100)

u_f1,v_f1,h_f1 = leapfrog(9.8, 1., 1., 10.)    
u_f10,v_f10,h_f10 = leapfrog(9.8, 10., 1., 10.)
u_f100,v_f100,h_f100 = leapfrog(9.8, 100., 1., 10.)

# lambda and H variation (H=5)
u_l5, v_l5, h_l5 = leapfrog(9.8, 0.0001, 0.5, 5.)

# gravity variation (g=4.9)
u_g49, v_g49, h_g49 = leapfrog(4.9, 0.0001, 1., 10.)


#%% Initial state
plt.figure(figsize=(8,6)) 
plt.plot(h_default[0,:,:].mean(axis=1))
plt.xlim(0,300)
plt.legend()
plt.xticks([0,75,150,225,300],[-100,-50,0,50,100])
plt.xlabel('x') ; plt.ylabel('h', rotation=0)
plt.title('Initial state')
plt.show()

#%% x-h plot
# without rotation effect plot
plt.figure(figsize=(12,12))
plt.suptitle('FTCS vs Leapfrog', fontsize=20)
for t in [50,100,150,200,250,300]:
    plt.subplot(3,2,int(t/50))
    plt.plot(h_ftcs_f0[t,:,:].mean(axis=1), label = 'FTCS')
    plt.plot(h_lf_f0[t,:,:].mean(axis=1), label = 'Leapfrog')
    plt.xlim(0,300)
    plt.legend()
    plt.text(170, h_ftcs_f0[t,:,:].mean(axis=1).max()*0.9, 't = '+str(t*dt))
    plt.xticks([0,75,150,225,300],[-100,-50,0,50,100])
    plt.xlabel('x') ; plt.ylabel('h', rotation=0)

plt.show()

# Rotation effect plot
plt.figure(figsize=(12,12))
plt.suptitle('Rotation effect', fontsize=20)
for t in [50,100,150,200,250,300]:
    plt.subplot(3,2,int(t/50))
    plt.plot(h_default[t,:,:].mean(axis=1), 'grey', label='f = 0.0001')
    plt.plot(h_f1[t,:,:].mean(axis=1), label = 'f = 1')
    plt.plot(h_f10[t,:,:].mean(axis=1), label = 'f = 10')
    plt.ylim(-2,2)
    plt.xlim(0,300)
    plt.legend()
    plt.text(160, 1.5, 't = '+str(t*dt))
    plt.xticks([0,75,150,225,300],[-100,-50,0,50,100])
    plt.xlabel('x') ; plt.ylabel('h', rotation=0)

plt.savefig('Rotation effect.png')
plt.show()

# Geopotential effect plot
plt.figure(figsize=(12,12))
plt.suptitle('Geopotential effect', fontsize=20)
for t in [50,100,150,200,250,300]:
    plt.subplot(3,2,int(t/50))
    plt.plot(h_default[t,:,:].mean(axis=1), 'grey', label='Λ = 1.0')
    plt.plot(h_l5[t,:,:].mean(axis=1), 'blue', label = 'Λ = 0.5')
    plt.ylim(-2,2)
    plt.xlim(0,300)
    plt.legend()
    plt.text(175,1.5,'t = '+str(t*dt))
    plt.xticks([0,75,150,225,300],[-100,-50,0,50,100])
    plt.xlabel('x') ; plt.ylabel('h', rotation=0)

plt.savefig('Geopotential effect.png')
plt.show()

# Gravity effect plot
plt.figure(figsize=(12,12))
plt.suptitle('Gravity effect', fontsize=20)
for t in [50,100,150,200,250,300]:
    plt.subplot(3,2,int(t/50))
    plt.plot(h_default[t,:,:].mean(axis=1), 'grey', label='g = 9.8')
    plt.plot(h_g49[t,:,:].mean(axis=1), 'blue', label = 'g = 4.9')
    plt.ylim(-2,2)
    plt.xlim(0,300)
    plt.legend()
    plt.text(175,1.5,'t = '+str(t*dt))
    plt.xticks([0,75,150,225,300],[-100,-50,0,50,100])
    plt.xlabel('x') ; plt.ylabel('h', rotation=0)

plt.savefig('Gravity effect.png')
plt.show()
  
#%% Stramplot for rotation variation
x_grid = np.linspace(0,300,301)
y_grid = np.linspace(0,300,301)

# default (f=0.0001)
plt.figure(figsize=(12,12))
plt.suptitle('Default parameter (f=0.0001)', fontsize=20)
for t in [50,100,150,200,250,300]:
    plt.subplot(3,2,int(t/50))
    plt.streamplot(x_grid, y_grid, u_default[t,:,:].T, v_default[t,:,:].T, color=h_default[t,:,:].T,
                   cmap='jet', density=0.5)
    plt.xticks([0,75,150,225,300],[-100,-50,0,50,100])
    plt.yticks([0,75,150,225,300],[-100,-50,0,50,100])
    plt.text(250,250,'t = '+str(t*dt), bbox=dict(facecolor='white', boxstyle='round'))
    plt.colorbar(label='h')
    plt.xlabel('x') ; plt.ylabel('y', rotation=0)
plt.savefig('streamline default.png')
plt.show()

# f = 1
plt.figure(figsize=(12,12))
plt.suptitle('Rotation variation (f = 1)', fontsize=20)
for t in [50,100,150,200,250,300]:
    plt.subplot(3,2,int(t/50))
    plt.streamplot(x_grid, y_grid, u_f1[t,:,:].T, v_f1[t,:,:].T, color=h_f1[t,:,:].T,
                   cmap='jet', density=0.5)
    plt.xticks([0,75,150,225,300],[-100,-50,0,50,100])
    plt.yticks([0,75,150,225,300],[-100,-50,0,50,100])
    plt.text(250,250,'t = '+str(t*dt), bbox=dict(facecolor='white', boxstyle='round'))
    plt.colorbar(label='h')
    plt.xlabel('x') ; plt.ylabel('y', rotation=0)
plt.savefig('streamline f1.png')
plt.show()

# f = 10
plt.figure(figsize=(12,12))
plt.suptitle('Rotation variation (f = 10)', fontsize=20)
for t in [50,100,150,200,250,300]:
    plt.subplot(3,2,int(t/50))
    plt.streamplot(x_grid, y_grid, u_f10[t,:,:].T, v_f10[t,:,:].T, color=h_f10[t,:,:].T,
                   cmap='jet', density=0.5)
    plt.xticks([0,75,150,225,300],[-100,-50,0,50,100])
    plt.yticks([0,75,150,225,300],[-100,-50,0,50,100])
    plt.xlim(0,300) ; plt.ylim(0,300)
    plt.text(250,250,'t = '+str(t*dt), bbox=dict(facecolor='white', boxstyle='round'))
    plt.colorbar(label='h')
    plt.xlabel('x') ; plt.ylabel('y', rotation=0)
plt.savefig('streamline f10.png')
plt.show()

