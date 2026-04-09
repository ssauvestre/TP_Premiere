"""
Activité expérimentale - Dégâts de la grêle

"""

import matplotlib.pyplot as plt  #import des bibliothèques nécessaires

""" Compléter les lignes 10 et 11 et indiquer un commentaire pour chacune d'elles """

m =      
g =      

z = [3.13, 2.92, 2.72, 2.51, 2.24, 1.90, 1.63, 1.36, 1.22] #liste altitudes
t = [0.04, 0.08, 0.12, 0.16, 0.20, 0.24, 0.28, 0.32, 0.36] #liste dates
v = [4.16, 4.32, 4.47, 4.76, 5.16, 5.54, 5.89, 6.11, 6.22] #listes vitesses

"""            Calculs des énergies              """

Ec = [0.5*m*V**2 for V in v]  #création de la liste énergie cinétique

""" Ci-dessous, créer la liste de l'énergie potentielle de pesanteur """


""" Ci-dessous, créer une liste vide de l'énergie mécanique puis réaliser une boucle 
permettant d'ajouter dans la liste chaque valeur de l'énergie méacanique calculée """



    
"""           Représentation graphique          """

plt.plot(t, Ec, marker = '+', color = 'red', label = 'Ec') # trace Ec=f(t)

""" Compléter le programme pour qu'il affiche les graphes Epp = f(t) et Em = f(t) """


""" Compléter les lignes 38, 39 et 40 afin qu'un titre et une legende des axes apparaissent """
plt.title ()  #titre du graphique
plt.xlabel () #légende axe des abscisses 
plt.ylabel () #légende axe des ordonnées
plt.legend() #affiche les légendes des courbes
plt.grid()  #affiche un quadrillage
plt.show()  #affiche le graphique





