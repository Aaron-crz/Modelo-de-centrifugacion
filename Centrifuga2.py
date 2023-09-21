import numpy as np
import matplotlib.pyplot as plt


"""Dfinimos las variables que ocupará nuestro programa"""
rho_p = 19300       #Densidad de la partícula (kg/m^3)
rho_m = 997       #Densidad del medio  (kg/m^3)
nu = 1.002e-3          #Viscosidad del fluido  (kg/m s)
r_0 = 9.0           #Radio inicial  (cm)
t = 1800            #Tiempo (seg)
omega1 = 1030 / 60
omega = 2290/60        #Velocidad angular (revs por seg)
omega2 = 3240/60
omega3 = 5620/60


def f(x):       #Definimos la funcion de centrifuagación
    dp1 = np.sqrt((18*np.log(x/r_0)*nu)/(t*(rho_p-rho_m)*omega1**2))    
    return dp1/1e-9

def g(x):       #Definimos la funcion de centrifuagación
    dp2 = np.sqrt((18*np.log(x/r_0)*nu)/(t*(rho_p-rho_m)*omega**2))    
    return dp2/1e-9

def h(x):       #Definimos la funcion de centrifuagación
    dp = np.sqrt((18*np.log(x/r_0)*nu)/(t*(rho_p-rho_m)*omega2**2))    
    return dp/1e-9

def j(x):       #Definimos la funcion de centrifuagación
    dp2 = np.sqrt((18*np.log(x/r_0)*nu)/(t*(rho_p-rho_m)*omega3**2))    
    return dp2/1e-9


#Limites y puntos
x = np.linspace(9,11.5,1000)
#v = [8,11.8,0,20000]

#Graficar
plt.plot(x,f(x),'b', label = '100 g')
plt.plot(x,g(x), 'y--', label = '500 g')
plt.plot(x,h(x),'r', label = '1000 g')
plt.plot(x,j(x),'c', label = '3000 g')



plt.xlabel('Radio (cm)')
plt.ylabel('Tamaño (nm)')
plt.title("Modelo de centrifugación 30 min")
plt.grid()
plt.legend(loc=2)
plt.text(9, 350, 'Sobrenadante')
plt.text(9.6, 450, 'Residual')
plt.text(10.55, 600, 'Pellet')

plt.axis()
#plt.axis(v)
plt.axvspan(9.0, 9.52, alpha=0.3, color='b')
plt.axvspan(9.52, 10.19, alpha=0.3, color='g')
plt.axvspan(10.19, 11.36, alpha=0.3, color='c')
