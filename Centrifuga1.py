import numpy as np
import matplotlib.pyplot as plt


"""Dfinimos las variables que ocupará nuestro programa"""
rho_p = 19300       #Densidad de la partícula (kg/m^3)
rho_m = 997       #Densidad del medio  (kg/m^3)
nu = 1.002e-3         #Viscosidad del fluido/agua (kg/m s)
r_0 = 9.0           #Radio inicial  (cm)
t1 = 600
t = 1800            #Tiempo (seg)
t2=3600
omega = 2290/60        #Velocidad angular (revs por seg)


def f(x):       #Definimos la funcion de centrifuagación
    dp1 = np.sqrt((18*np.log(x/r_0)*nu)/(t1*(rho_p-rho_m)*omega**2))    
    return dp1/1e-9

def h(x):       #Definimos la funcion de centrifuagación
    dp = np.sqrt((18*np.log(x/r_0)*nu)/(t*(rho_p-rho_m)*omega**2))    
    return dp/1e-9

def g(x):       #Definimos la funcion de centrifuagación
    dp2 = np.sqrt((18*np.log(x/r_0)*nu)/(t2*(rho_p-rho_m)*omega**2))    
    return dp2/1e-9


#Limites y puntos
x = np.linspace(9,11.5,1000)
#v = [8,11.8,0,20000]

#Graficar
plt.plot(x,f(x),'b', label = '10 min')
plt.plot(x,h(x), 'y--', label = '30 min')
plt.plot(x,g(x),'r', label = '60 min')



plt.xlabel('Radio (cm)')
plt.ylabel('Tamaño (nm)')
plt.title("Modelo de centrifugación 500 g")
plt.grid()
plt.legend(loc=2)
plt.text(9, 250, 'Sobrenadante')
plt.text(9.6, 350, 'Residual')
plt.text(10.55,500, 'Pellet')
plt.axis()
#plt.axis(v)
plt.axvspan(9.0, 9.52, alpha=0.3, color='b')
plt.axvspan(9.52, 10.19, alpha=0.3, color='g')
plt.axvspan(10.19, 11.36, alpha=0.3, color='c')

