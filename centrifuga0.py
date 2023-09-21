# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 10:44:34 2023
Tiempo de sedimentación  
@author: aaron cruz
"""
import numpy as np

##Para obteer el tiempo de sedimentacion bajo Fuerza de gravedad CONSTANTE (caida libre)
##de una particula de oro de diametro dp en agua
Fg = 9.81        ## m/s^2
rho_l = 0.997    ## kg/m^3
rho_p = 19300    ## kg/m^3
d = 1e-2         ## m
nu = 0.01002     ## Pa s
dp = 10e-9       ## m

t = (18*nu*d)/(dp**2*abs(rho_l-rho_p)*Fg)

print("El tiempo en el que una partícula de diametro ", dp/1e-9, "nm  \n recorre ",  d/1e-2, "cm en caida libre es de: \n", round(t,2), "Seg")
print("equivalente a: \n", round(t/60,2), "min \n", round(t/3600,2), "hrs \n", round(t/86400,2), "dias")

##Ahora obtendremos el tiempo en sedimentarse bajo una aceleracion VARIABLE como es el
##Caso de un coloide de partoiculas acelerado por una centrifuga
##Datos especificos para el experimento:
"""Centrifugadora Hermle z206 a con un radio de rotor al inicio de l tubo eppendorf
de 8.49 cm... asumimos que la distancia recorrida será la misma que el caso de caida libre
pero en este caso se aplica una aceleracion omega"""

r0 = 8.49e-2      ## m
rf = r0+d
omega = 2290/60    ##vueltas/seg

t2 = (18*np.log(rf/r0)*nu)/(dp**2*(abs(rho_l-rho_p))*omega**2) 

print("Por otro lado, en una centrifuga Hermle z206a con una aceleracion", round(omega,2), "rev/seg \n El tiempo que la misma partícula tarda en recorrer ", d/1e-2, "cm es de" )
print(round(t2,2), "seg")
print(round(t2/60,2), "min")
print(round(t2/3600,2), "hrs")
print(round(t2/86400,2), "dias")




