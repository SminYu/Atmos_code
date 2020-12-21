# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:52:12 2020

@author: YSM
"""

import numpy as np
import matplotlib.pyplot as plt

n0=300.
sigma=4.0
am=5.0
pi=np.pi
nn=1000

a=np.zeros(nn)
dndloga=np.zeros(nn)
dSdloga=np.zeros(nn)
dMdloga=np.zeros(nn)

for i in range(nn):
    a[i]=i+1
    dndloga[i]=n0/np.log(sigma)/np.sqrt(2*pi)*np.exp(-((np.log(a[i]/am))**2)/2/(np.log(sigma))**2)
    dSdloga[i]=dndloga[i]*4*pi*((a[i]*10**-6)**2)
    dMdloga[i]=dndloga[i]*4/3*pi*((a[i]*10**-6)**3)*1.293

fig1=plt.figure(figsize=(12,8))
ax1=fig1.add_subplot(111)
ax1.set_xlabel('a (um)')
ax1.set_ylabel('dn/d(loga)')
plt.plot(a,dndloga)

fig2=plt.figure(figsize=(12,8))
ax2=fig2.add_subplot(111)
ax2.set_xlabel('a (um)')
ax2.set_ylabel('dS/d(loga)')
plt.plot(a,dSdloga)

fig3=plt.figure(figsize=(12,8))
ax3=fig3.add_subplot(111)
ax3.set_xlabel('a (um)')
ax3.set_ylabel('dM/d(loga)')
plt.plot(a,dMdloga)