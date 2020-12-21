"""
Pseudo-adiabatic chart
Created on Thu May 28 22:45:21 2020
@author: YSM

0 degree celsius = 273 Kelvin
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#사용할 상수 
Psfc=1000.
kappa=0.286 #Rd/Cpd=0.286
epsilon=0.622 #Mv/Md = 0.622
latent=2.50*10**6 #물의 vaporization latent heat = 2.50*10^6J/kg
R_v=461.51 
ec0=6.11 #물의 삼중점에서의 포화수증기압 6.11hPa
T0=273.16 #물의 삼중점에서의 온도 273.16K
P0=1013.25 #표준대기압 1013.25hPa
cpd=1005.
r_w0=epsilon*ec0/P0

# x는 기압, y는 온도
# 1013hPa~200hPa이라 814개, 203K~308K이라 106개
pp=814
tt=106

P=np.zeros([pp,tt])
T=np.zeros([pp,tt])
theta=np.zeros([pp,tt])
theta_e=np.zeros([pp,tt])
r_w=np.zeros([pp,tt])

for i in range(pp):
    P[i,:]=200+i
for j in range(tt):
    T[:,j]=203+j

#%% 온위, 포화수증기압, 상당온위 계산
for i in range(pp):
    for j in range(tt):  
        theta[i,j]=T[i,j]*(Psfc/P[i,j])**kappa #온위
        r_w[i,j]=r_w0*(np.exp(-latent/R_v*((1/T[i,j])-(1/T0))))/(P[i,j]/P0) #포화수증기압
        theta_e[i,j]=theta[i,j]*np.exp(latent*r_w[i,j]/cpd/T[i,j]) #상당온위
#%% chart plot

fig=plt.figure(figsize=(12,12))
ax1=fig.add_subplot(111)
ax1.set_xlabel('Temperature (K)') ; ax1.set_xlim(203,308) #203K부터 308K까지
ax1.set_ylabel('Pressure (hPa)') ; ax1.set_ylim(1013,200) #기압은 1013hPa부터 200hPa까지 (반전)

#y축을 지수적으로 조정해 단열선을 직선으로 만드는 과정
#y축을 x^k로 바꿈
def forward(x):
    return x**(kappa) 
def inverse(x):
    return x**(1./kappa)
ax1.set_yscale('function', functions=(forward, inverse))

#온위, 포화수증기압, 상당온위의 그래프를 그리는 과정 
CS1 = ax1.contour(T,P,theta, levels = np.arange(210,430,10),colors='black')
ax1.clabel(CS1, inline=1, fontsize=10, fmt='%1.0f')
r_wlevel= np.array([0.1,0.2,0.5,1.,1.5,2.,3.,4.,6.,8.,10.,12.,15.,20.,25.,30.])
CS2 = ax1.contour(T,P,1000*r_w, levels = r_wlevel,colors='grey') #포화혼합비 단위 g/g에서 g/kg으로 변환하기 위해 1000을 곱함
ax1.clabel(CS2, inline=1, fontsize=10,fmt='%1.2f')
CS3 = ax1.contour(T,P,theta_e, levels = np.arange(210,410,10),linestyles='dashed',colors='black')
ax1.clabel(CS3, inline=1, fontsize=10, fmt='%1.0f')
plt.title('Pseudo-adiabatic chart')
plt.show()

#%%data.csv파일을 불러오기
#파일 불러오고 데이터를 저장
f1=pd.read_csv('data.csv',delimiter=',',header=None)
f2=f1.to_numpy()
#온도와 이슬점온도를 기압에 대한 데이터로 저장
temp=np.zeros([pp,2])
dewT=np.zeros([pp,2])
rrrr=np.zeros([pp,2])

for i in range(pp-6): #1013부터 1008까지는 결측
    temp[i+6,0]=f2[i,0]
    temp[i+6,1]=273+f2[i,1]
    dewT[i+6,0]=f2[i,0]
    dewT[i+6,1]=273+f2[i,2]
    rrrr[i+6,0]=f2[i,0]
    rrrr[i+6,1]=1000.*r_w0*(np.exp(-latent/R_v*((1/dewT[i+6,1])-(1/T0))))/(f2[i,0]/P0) #이 때, r의 단위 g/kg으로
    
r_sum=0.
for i in range(pp-6):
    r_sum=r_sum+rrrr[i+6,1] #p에 대해 r을 적분하기 위해 1hPa 간격의 자료를 더함
r_sum=100.*r_sum #p의 간격이 1hPa(=100Pa)이므로 r의 합에 100을 곱한 값은 적분과 같음
prvap=r_sum/9.8 #precipitable water vapor = r의 적분 / g(중력가속도)
print ('Precipitable water vapor =',prvap,'g/m2') #precipitable water vapor의 단위는 g/m2

#위에서 그린 emagram 그대로 사용       
fig=plt.figure(figsize=(12,12))
ax1=fig.add_subplot(111)
ax1.set_xlabel('Temperature (K)') ; ax1.set_xlim(203,308)
ax1.set_ylabel('Pressure (hPa)') ; ax1.set_ylim(1013,200)

def forward(x):
    return x**(kappa)
def inverse(x):
    return x**(1./kappa)
ax1.set_yscale('function', functions=(forward, inverse))
CS1 = ax1.contour(T,P,theta, levels = np.arange(210,430,10),colors='black')
ax1.clabel(CS1, inline=1, fontsize=10, fmt='%1.0f')
r_wlevel= np.array([0.1,0.2,0.5,1.,1.5,2.,3.,4.,6.,8.,10.,12.,15.,20.,25.,30.])
CS2 = ax1.contour(T,P,1000*r_w, levels = r_wlevel,colors='grey')
ax1.clabel(CS2, inline=1, fontsize=10,fmt='%1.2f')
CS3 = ax1.contour(T,P,theta_e, levels = np.arange(210,410,10),linestyles='dashed',colors='black')
ax1.clabel(CS3, inline=1, fontsize=10, fmt='%1.0f')
#관측 기온과 이슬점 기입
CS4 = ax1.plot(temp[6:,1],temp[6:,0],linewidth=3.0,label='Temperature (K)') #1007hPa부터 시작
CS5 = ax1.plot(dewT[6:,1],dewT[6:,0],linewidth=3.0,label='Dew-point temperature (K)')

plt.legend()
plt.title('Pseudo-adiabatic chart')

plt.show()

#%% LCL 찾기
#air parcel P=1007hPa, T=14.8C=288K, Td=10.8C=284K
#At LCL(r=rw), P=? & T=?

#주어진 조건에서의 r 찾기
r_i=r_w0*(np.exp(-latent/R_v*((1/dewT[7,1])-(1/T0))))/(1007./P0)

#lCL 찾기. (온위는 같고 rw=ri인 지점)
for i in range(pp):
    for j in range(tt):
        if (abs((theta[i,j]-theta[807,85])/theta[807,85])<0.002): #==를 사용하면 오차범위 안에 있는 가능한 모든 경우의 수 판단 불가능.
            if (abs((r_w[i,j]-r_i)/r_i)<0.001):
                LCL_1=i
                LCL_2=j
                print ('Pressure of LCL =',P[i,j],'hPa') #LCL의 기압, 온도
                print ('Temperature of LCL =',T[i,j],'K') 

#LCl에서 습윤단열감률로 상승
#습윤단열선 따라 상승하는 공기덩어리의 온도선 temp2는 압력과 온도 성분으로 이루어짐
temp2=np.empty([pp,2])
for i in range(pp):
    for j in range(tt):
        if (abs((theta_e[i,j]-theta_e[LCL_1,LCL_2])/theta_e[LCL_1,LCL_2])<0.01):
            temp2[i,0]=P[i,j]
            temp2[i,1]=T[i,j]

            
#%%air parcel path plot
fig=plt.figure(figsize=(12,12))
ax1=fig.add_subplot(111)
ax1.set_xlabel('Temperature (K)') ; ax1.set_xlim(203,308)
ax1.set_ylabel('Pressure (hPa)') ; ax1.set_ylim(1013,200)

def forward(x):
    return x**(kappa)
def inverse(x):
    return x**(1./kappa)
ax1.set_yscale('function', functions=(forward, inverse))

CS1 = ax1.contour(T,P,theta, levels = np.arange(210,430,10),colors='black')
ax1.clabel(CS1, inline=1, fontsize=10, fmt='%1.0f')
r_wlevel= np.array([0.1,0.2,0.5,1.,1.5,2.,3.,4.,6.,8.,10.,12.,15.,20.,25.,30.])
CS2 = ax1.contour(T,P,1000*r_w, levels = r_wlevel,colors='grey')
ax1.clabel(CS2, inline=1, fontsize=10,fmt='%1.2f')
CS3 = ax1.contour(T,P,theta_e, levels = np.arange(210,410,10),linestyles='dashed',colors='black')
ax1.clabel(CS3, inline=1, fontsize=10, fmt='%1.0f')
CS4 = ax1.plot(temp[6:,1],temp[6:,0],linewidth=3.0,label='Temperature (K)')
CS5 = ax1.plot(dewT[6:,1],dewT[6:,0],linewidth=3.0,label='Dew point(K)')
#지상으로부터 LCL까지의 건조기압감률선을 따라 이동한 plot
CS6 = ax1.plot([T[807,85],T[LCL_1,LCL_2]],[P[807,85],P[LCL_1,LCL_2]],linewidth=3.0,c='g')
#LCL부터 습윤단열감률선을 따라 이동한 plot
CS7 = ax1.plot(temp2[:LCL_1,1],temp2[:LCL_1,0],linewidth=3.0,c='g',label='Air parcel temperature (K)')
plt.legend()
plt.title('Pseudo-adiabatic chart')
plt.show()