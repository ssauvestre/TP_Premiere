"""Suite de l'activité expérimentale : Trajectoire d'une balle"""

import numpy as np # import d'une bibliothèque permettant un traitement 
# numérique rapide et efficace
import matplotlib.pyplot as plt # import d'une bibliothèque math permettant
# de tracer un graphique

# Positions d'une balle obtenues par pointage vidéo
""" CI-DESSOUS !! Ajouter les valeurs des coordonnées de la balle en X et en Y """
""" Donnée : les valeurs sont séparées d'une virgule et un nombre décimal s'écrit avec un point """
X=[] # ensemble des coordonnées en abscisse
Y=[] # ensemble des coordonnées en ordonnée
t=np.linspace(0,0.36,10) # associe 10 valeurs de tps de 0 s à 0,36 s 

plt.plot(X, Y, color = 'green', marker ='o') 

""" CI-DESSOUS !! Compléter l'instruction afin d'ajouter un titre au graphique """ 
plt.title("")

plt.ylabel("Y (m)") 

"""  CI-DESSOUS !! Coder l'instruction pour tracer la légende de l'axe des X""" 


