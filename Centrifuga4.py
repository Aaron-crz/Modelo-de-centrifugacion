import numpy as np
import matplotlib.pyplot as plt


"""Dfinimos las variables que ocupará nuestro programa"""
rho_p = 19300       #Densidad de la partícula (kg/m^3)
rho_m = 997       #Densidad del medio  (kg/m^3)
nu = 1.002e-3         #Viscosidad del fluido/agua (kg/m s)
r_0 = 9.0           #Radio inicial  (cm)
r_p = 10.19

omega1 = 1030/60        #Velocidad angular (revs por seg)
omega2 = 2290/60
omega3 = 3240/60
omega4 = 5620/60
omega5 = 7250/60


def f(x):       #Definimos la funcion de centrifuagación
    dp1 = np.sqrt((18*np.log(r_p/r_0)*nu)/(x*(rho_p-rho_m)*omega1**2))    
    return dp1/1e-9
def g(x):       #Definimos la funcion de centrifuagación
    dp1 = np.sqrt((18*np.log(r_p/r_0)*nu)/(x*(rho_p-rho_m)*omega2**2))    
    return dp1/1e-9
def h(x):       #Definimos la funcion de centrifuagación
    dp1 = np.sqrt((18*np.log(r_p/r_0)*nu)/(x*(rho_p-rho_m)*omega3**2))    
    return dp1/1e-9
def i(x):       #Definimos la funcion de centrifuagación
    dp1 = np.sqrt((18*np.log(r_p/r_0)*nu)/(x*(rho_p-rho_m)*omega4**2))    
    return dp1/1e-9
def j(x):       #Definimos la funcion de centrifuagación
    dp1 = np.sqrt((18*np.log(r_p/r_0)*nu)/(x*(rho_p-rho_m)*omega5**2))    
    return dp1/1e-9




#Limites y puntos
x = np.linspace(2,5000,10000)
v = [0,5020,0,520]

#Graficar
plt.plot(x,f(x),'b', label = '100 g')
plt.plot(x,g(x),'g', label = '500 g')
plt.plot(x,h(x),'r', label = '1000 g')
plt.plot(x,i(x),'c', label = '3000 g')
plt.plot(x,j(x),'m', label = '5000 g')


plt.xlabel('tiempo (s)')
plt.ylabel('Tamaño (nm)')
plt.title("Evolución temporal")
plt.grid()
plt.legend(loc=1)

"""plt.text(9, 250, 'Sobrenadante')
plt.text(9.6, 350, 'Residual')
plt.text(10.55,500, 'Pellet')"""

plt.axis()
plt.axis(v)
"""plt.axvspan(9.0, 9.52, alpha=0.3, color='b')
plt.axvspan(9.52, 10.19, alpha=0.3, color='g')
plt.axvspan(10.19, 11.36, alpha=0.3, color='c')"""
