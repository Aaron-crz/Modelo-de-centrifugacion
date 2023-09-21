import numpy as np
import matplotlib.pyplot as plt


"""Dfinimos las variables que ocupará nuestro programa"""
rho_p = 19300       #Densidad de la partícula (kg/m^3)
rho_et = 789       #Etanol
rho_peg = 1130           #Polietilglycol
rho_gli = 1260            #Glicerina
rho_ac = 1840           #Acido sulfurico
rho_merc = 13600         #mercurio
rho_m = 997       #Densidad del medio (agua) (kg/m^3)

nu_et = 1.074e-3
nu_peg = 0.0161
nu_gli = 1.5
nu_ac = 0.0242
nu_merc = 1.526e-3
nu = 1.002e-3          #Viscosidad del fluido  (kg/m s)

r_0 = 9.0           #Radio inicial  (cm)
t = 1800            #Tiempo (seg)
omega = 2290/60        #Velocidad angular (revs por seg)


def f(x):       #Definimos la funcion de centrifuagación
    dp1 = np.sqrt((18*np.log(x/r_0)*nu_et)/(t*(rho_p-rho_et)*omega**2))    
    return dp1/1e-9

def g(x):       #Definimos la funcion de centrifuagación
    dp2 = np.sqrt((18*np.log(x/r_0)*nu_peg)/(t*(rho_p-rho_peg)*omega**2))    
    return dp2/1e-9

def h(x):       #Definimos la funcion de centrifuagación
    dp = np.sqrt((18*np.log(x/r_0)*nu_gli)/(t*(rho_p-rho_gli)*omega**2))    
    return dp/1e-9

def j(x):       #Definimos la funcion de centrifuagación
    dp2 = np.sqrt((18*np.log(x/r_0)*nu_ac)/(t*(rho_p-rho_ac)*omega**2))    
    return dp2/1e-9

def k(x):       #Definimos la funcion de centrifuagación
    dp2 = np.sqrt((18*np.log(x/r_0)*nu_merc)/(t*(rho_p-rho_merc)*omega**2))    
    return dp2/1e-9

def l(x):       #Definimos la funcion de centrifuagación
    dp2 = np.sqrt((18*np.log(x/r_0)*nu)/(t*(rho_p-rho_m)*omega**2))    
    return dp2/1e-9


#Limites y puntos
x = np.linspace(9,11.5,1000)
#v = [8,11.8,0,20000]

#Graficar
plt.plot(x,f(x),'b', label = 'Etanol')
plt.plot(x,g(x), 'y', label = 'Etilglycol')
#plt.plot(x,h(x),'r', label = 'glicerina')
plt.plot(x,j(x),'m', label = 'Acido sulfurico')
plt.plot(x,k(x),'k', label = 'mercurio')
plt.plot(x,l(x),'w--', label = 'agua')



plt.xlabel('Radio (cm)')
plt.ylabel('Tamaño (nm)')
plt.title("Modelo de centrifugación diferentes medios")
plt.grid()
plt.legend(loc=2)
plt.text(9, 10, 'Sobrenadante')
plt.text(9.6, 16, 'Residual')
plt.text(10.55, 2, 'Pellet')

plt.axis()
#plt.axis(v)
plt.axvspan(9.0, 9.52, alpha=0.3, color='b')
plt.axvspan(9.52, 10.19, alpha=0.3, color='g')
plt.axvspan(10.19, 11.36, alpha=0.3, color='c')