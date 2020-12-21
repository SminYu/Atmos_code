"""
Created on Sat Jun 13 09:35:21 2020

@author: YSM
"""

import numpy as np
import matplotlib.pyplot as plt

pi=np.pi
Ls=2.83E+06 #Latent heat of sublimitation to ice
Rv=461.51 #Gas constant of water vapor
C=1. #구름 입자 유형에 따라 달라지는 값

tt=401 #0.1도 단위로 나누기 (0도부터 40.0도까지 401개)
pp=3

Temp=np.zeros(tt)
Temp2=np.zeros(tt)
K=np.zeros(tt)
D=np.zeros([tt,pp])
dmdt=np.zeros([tt,pp])
ei=np.zeros(tt)
es=np.zeros(tt)

P=[1000.*50., 1000.*75., 1000*100.] #50kPa, 75kPa, 100kPa에서
x1=[0,100,200,300,400] #0.1도 단위이므로 간격은 100
y1=[2.40E-2,2.32E-2,2.24E-2,2.16E-2,2.07E-2] #reference의 K값
y2=[2.21E-5,2.06E-5,1.91E-5,1.76E-5,1.62E-5] #refernce의 D값
Tinterp=np.arange(tt)
K=np.interp(Tinterp,x1,y1) #K를 interpolation해서 연속적인 값으로 만든다

for j in range (pp):
    D[:,j]=(np.interp(Tinterp,x1,y2))*(100./(P[j]/1000.))  #D를 interpolation해서 연속적인 값으로 변환
    #D values are for pressure 100kPa and inversely propotional to pressure
    #So we multiply (100/p) for kPa unit(1000Pa=1kPa)
    
    for i in range(tt):
        Temp[i] = 0.1*float(i) #섭씨온도 절댓값 (영하 20도면 20)
        Temp2[i] = 273.15-0.1*float(i) #절대온도
        
        ei=(6.11E+02)*np.exp(2.83E+06/461.51*((1/273.16)-(1/Temp2[i]))) #얼음 포화수증기압
        es=(6.11E+02)*np.exp(2.50E+06/461.51*((1/273.16)-(1/Temp2[i]))) #물 포화수증기압
        Si=es/ei
        dmdt[i,j]=(4*pi*(Si-1))/((Ls/Rv/Temp2[i]-1)*(Ls/K[i]/Temp2[i])+(Rv*Temp2[i]/ei/D[i,j]))

fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111)
ax.set_xlabel('Temperauture(ºC)') ; ax.set_xlim(0,-40.)
ax.set_ylabel('Normalized dm/dt')

f2=plt.plot(-Temp,(dmdt[:,0]*1.0E+08/(4*pi*C)),label='50kPa')
f2=plt.plot(-Temp,(dmdt[:,1]*1.0E+08/(4*pi*C)),label='75kPa')
f2=plt.plot(-Temp,(dmdt[:,2]*1.0E+08/(4*pi*C)),label='100kPa')
f2=plt.axvline(x=-15., c='r')

plt.legend()
plt.title('Normalized ice crystal growth rate')
plt.show()
