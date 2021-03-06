# -*- coding: utf-8 -*-
"""PropagaciónCampoE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1442diXDAIWaQDAorYAiT4An50nYh1rGf
"""

#matplotlib qt



#PROPAGACIÓN DE CAMPO ELÉCTRICO EN DIELÉCTRICOS
#punto 1

#importación de librerias:
import numpy as np 
import matplotlib.pyplot as plt

alpha = 1e-7 #@param {type: "slider", min: 0, max: 0.000002, step: 0.0000001}
f = 1001 # 
T = 1/f # periodo de la onda
v = 3e8 # velocidad de propagación de la onda
epsilon_r = 2.6 # permitividad relativa
epsilon_0 = 8.85e-12 # permitividad del espacio libre
epsilon = epsilon_r*epsilon_0
mu_r = 1 # permeabilidad relativa
mu_0 = 4e-12*np.pi# permeabilidad del espacio libre
mu = mu_r*mu_0
lambd = v/f # longitud de la onda
omega = 2*np.pi*f # frecuencia en radianes
#beta = omega*np.sqrt(epsilon*mu) #beta calculado a partir de mu y epsilon
beta = (2*np.pi)/lambd
if (alpha!=0): delta = 1/alpha # profundidad de penetración
else: delta=0
z = np.arange(0,1000000,100) # dirección de propagación
envolvente = np.exp(-alpha*z) # envolvente de la onda 
cs = np.cos(beta*z) # onda coseno
Ez = envolvente*cs # onda resultante

# graficación
rectangulo = plt.Rectangle((0,-1.2),delta,2.4,color='#77F2D4',alpha=.3) #creación del rectangulo

fig, ax = plt.subplots(1,2,figsize=(18,6))
ax[0].axis([0,z[-1],-1.2,1.2])
ax[0].plot(z,envolvente, 'b-.',label = 'envolvente')
ax[0].plot(z, cs, label='Coseno',color='#FF0000',lw=2)
ax[0].set_xlabel('Distancia z (m)', fontsize=14)
ax[0].set_ylabel('E [V/m]', fontsize=14)
ax[0].legend(loc='lower right')
ax[0].set_facecolor('.95') # corregimos el color de fondo
ax[0].grid(True, linestyle='-.', color='.3',lw=.5) # ponemos una malla

ax[1].axis([0, z[-1], -1.2, 1.2])
ax[1].add_artist(rectangulo)
ax[1].plot(z, envolvente, 'b-.',label='Envolvente')
ax[1].plot([0, z[-1]], [0.37, 0.37], 'k--', lw=1, label='0.37')
ax[1].plot(z, Ez, label='Campo eléctrico', lw=3,color='#FF0000')
ax[1].set_xlabel('Distancia z (m)', fontsize=14)
ax[1].legend(loc='lower right')
ax[1].set_facecolor('.95') # corregimos el color de fondo
ax[1].grid(True, linestyle='-.', color='.3',lw=.5) # ponemos una malla

fig.show()

"""Punto 2"""
f = 1e3
epsilon_r = 1
mu_r = 1
sigma = 5.8e7
alpha = np.sqrt(np.pi*epsilon_r*mu_r*f)
beta = np.sqrt(np.pi*epsilon_r*mu_r*f)
omega = 2*np.pi*f
z = np.arange(0,.2,.001)
envolvente = np.exp(-alpha*z) # envolvente de la onda 
cs = np.cos(beta*z) # onda coseno
Ez = envolvente*cs # onda resultante

# graficación
rectangulo = plt.Rectangle((0,-1.2),delta,2.4,color='#77F2D4',alpha=.3)

fig, ax = plt.subplots(1,2,figsize=(18,6))
ax[0].axis([0,z[-1],-1.2,1.2])
ax[0].plot(z,envolvente, 'b-.',label = 'envolvente')
ax[0].plot(z, cs, label='Coseno',color='#FF0000',lw=3)
ax[0].set_xlabel('Distancia z (m)', fontsize=14)
ax[0].set_ylabel('E [V/m]', fontsize=14)
ax[0].legend(loc='lower right')
ax[0].set_facecolor('.95') # corregimos el color de fondo
ax[0].grid(True, linestyle='-.', color='.3',lw=.5) # ponemos una malla


ax[1].axis([0, z[-1], -1.2, 1.2])
ax[1].add_artist(rectangulo)
ax[1].plot(z, envolvente, 'b-.',label='Envolvente')
ax[1].plot([0, z[-1]], [0.37, 0.37], 'k--', lw=1, label='0.37')
ax[1].plot(z, Ez, label='Campo eléctrico', lw=3,color='#FF0000')
ax[1].set_xlabel('Distancia z (m)', fontsize=14)
ax[1].legend(loc='lower right')
ax[1].set_facecolor('.95') # corregimos el color de fondo
ax[1].grid(True, linestyle='-.', color='.3',lw=.5) # ponemos una malla

fig.show()

import numpy as np
import matplotlib.pyplot as plt

Frecuencia_PHz = 9001 #@param {type: "slider", min: 1, max: 10000, step: 1000}
Radio_nm = 10  #@param {type: "slider", min: 1, max: 10}

e0 = 8.8542e-12;
u0 = 1.2566e-6;
er = 1;
ur = 1;
sigma = 5.96e7;
Radio = Radio_nm*1e-9;

omega = 2*np.pi*Frecuencia_PHz*1e15;
e = e0*er;
u = u0*ur;
tand = sigma/(omega*e);
alpha = omega*np.sqrt(u*e/2)*np.sqrt(np.sqrt(1+tand**2)-1);
beta  = omega*np.sqrt(u*e/2)*np.sqrt(np.sqrt(1+tand**2)+1);
delta = 1/alpha
lambd = 2*np.pi/beta
z = np.arange(0, Radio, Radio/100000)
Env = np.exp(-alpha*z)
Ezp = Env*np.cos(-beta*z)
if delta>=Radio:
  Rin = Radio
else:
  Rin = delta

f, ax = plt.subplots(1, 2, figsize=(12, 6))
rec_r = plt.Rectangle((0, -1.2), 1, 2.4, color='#A9FF99',alpha=0.3)
rec_b = plt.Rectangle((Rin/Radio, -1.2), 1-Rin/Radio, 2.4, color='#22D700',alpha=0.3)

ax[0].add_artist(rec_r)
ax[0].add_artist(rec_b)
ax[0].plot(z/Radio, Ezp,label='E',lw=3)
ax[0].plot(z/Radio, Env,'k--',label='Envolvente',lw=1)
ax[0].plot([0, 1], [0.37, 0.37], 'r--', lw=1, label='0.37')
ax[0].axis([0, 1, -1.2, 1.2])
ax[0].set_xlabel('Longitud z/Radio', fontsize=14)
ax[0].set_ylabel('E (V/m)', fontsize=14)
ax[0].legend()
ax[0].set_title('Onda eléctrico en el conductor', fontsize=14)
ax[0].set_facecolor('.95') # corregimos el color de fondo
ax[0].grid(True, linestyle='-.', color='.3',lw=.5) # ponemos una malla

cir_total = plt.Circle((0, 0), Radio*1e9, color='#A9FF99', alpha=0.3)
cir_piel = plt.Circle((0, 0), (Radio-Rin)*1e9, color='#22D700', alpha=0.3)

ax[1].axis([-12, 12, -12, 12])
ax[1].add_artist(cir_total)
ax[1].add_artist(cir_piel)
ax[1].set_xlabel('Longitud $ nm$', fontsize=14)
ax[1].set_ylabel('Longitud $ nm$', fontsize=14)
ax[1].set_title('Efecto piel en conductor', fontsize=14)
ax[1].set_facecolor('.95') # corregimos el color de fondo



f.suptitle('Efecto piel: radio %.3f nm ; delta %.3f nm' % (Radio/1e-9,delta/1e-9), fontsize=14)
f.show()
print('radio : %.3f um ; delta : %.3f um' % (Radio/1e-6,delta/1e-6))
print(tand)
print("sigma"+ str(sigma) +"\nomega: "+ str(omega))

import numpy as np
import matplotlib.pyplot as plt

Frecuencia_PHz = 7001  #@param {type: "slider", min: 1, max: 10001, step: 1000}

f = Frecuencia_PHz*1e15;
e0 = 8.8542e-12;
u0 = 1.2566e-6;
er = 1;
ur = 1;
sigma = 5.8e7;

omega = 2*np.pi*f;
e = e0*er;
u = u0*ur;
tand = sigma/(omega*e);
alpha = omega*np.sqrt(u*e/2)*np.sqrt(np.sqrt(1+tand*2)-1);
beta  = omega*np.sqrt(u*e/2)*np.sqrt(np.sqrt(1+tand*2)+1);
delta = 1/alpha
lambd = 2*np.pi/beta

z = np.arange(0,u, e*1e-1)
Env = np.exp(-alpha*z)
senal = Env*np.cos(-beta*z)

f, ax = plt.subplots( figsize=(12, 6))

rec_r = plt.Rectangle((0, -1.2), 3, 2.4, color='#fff616', alpha = 0.3)
rec_b = plt.Rectangle((delta/lambd, -1.2), 3-delta/lambd, 2.4, color='#bfffb1')

ax.add_artist(rec_r)
ax.add_artist(rec_b)
ax.plot(z/lambd, senal,color = '#0c009a', label='E',lw=2)
ax.plot(z/lambd, Env,'k--',label='Envolvente',lw=2)
ax.plot([0, 3], [0.37, 0.37], 'r--', lw=2, label='0.37')
ax.axis([0, 3, -1.2, 1.2])
ax.grid(color = 'k', alpha = 0.3)
ax.set_xlabel('Longitud z', fontsize=14)
ax.set_ylabel('E (V/m)', fontsize=14)
ax.legend()
ax.set_title('Onda eléctrico en el conductor', fontsize=14)
print("Tand : {:.4f}".format(tand ))
print("sigma"+ str(sigma) +"\nomega: "+ str(omega))
fig.show()

