
"""
Activité expérimentale : Influence de la masse sur le vecteur variation de vitesse à l’aide d’un programme Python

"""
import matplotlib.pyplot as plt
import numpy as np

""" Partie 1 : Valeurs manquantes du tableau """

# création de listes pour la masse marquée, la vitesse atteinte au bout de 200 ms et 500 ms
M = [300, 400, 500, 600, 700] # en g
v_200ms = [0.40, 0.34, 0.32, 0.31, 0.28] # en m/s
v_500ms = [0.81, 0.68, 0.59, 0.56, 0.51] # en m/s
m_syst = [] # en kg
dv = [] # en m/s
dv_sur_dt = [] # en m/s²

" Compléter les instructions dans la boucle ci-dessous "
for i in range(0,len(M)):
    m_syst.append()
    dv.append()
    dv_sur_dt.append()
    
""" Ci-dessous, compléter le programme pour afficher les différentes masses du système, 
les valeurs de la variation de vitesse et l'ensemble des valeurs ∆v/∆t
"""
    

""" Partie 2 : Tracé du graphique permettant de tester la relation approchée de la 2ème loi de Newton """

plt.plot()
plt.title()
plt.ylabel() 
plt.xlabel() 


""" Partie 3 : Modélisation de la droite par une fonction linéaire """

inv_M=np.array(inv_M)   # on change inv_M de type pour le passer en array
dv_sur_dt=np.array(dv_sur_dt)

coeff_model=np.polyfit(inv_M, dv_sur_dt,1)

ymod = coeff_model[0]*inv_M**1 + coeff_model[1]

plt.plot(inv_M, ymod, 'r-')

plt.axis([0, 2, 0, 1.5])

plt.show()
   