""" ICI !! Commenter la ligne suivante avec # """
import matplotlib.pyplot as plt

"""     1ère partie -  ENTREE DES PARAMETRES    -    """

""" ICI !! commenter la ligne suivante avec # """
print("SIMULATION DE L'EVOLUTION D'UN SYSTEME CHIMIQUE LIEU D'UNE TRANSFORMATION TOTALE ")
print("Entrer  :")
print("  - les quantités de matière initiales des deux réactifs A et B et des deux produits C et D")
print("  - les nombres stoechiometriques de la réaction : a A + b B = c C + d D")

""" ICI !! commenter la ligne suivante avec # """
niA = float(input("ni(A) en mol ? ")) 
niB = float(input("ni(B) en mol ? ")) 
""" ICI !! coder l'instruction pour calculer la qté de matière de C """
""" ICI !! coder l'instruction pour calculer la qté de matière de D """

""" ICI !! commenter la ligne suivante avec # """
a = int(input(" a (entier naturel) ? "))
b = int(input(" b (entier naturel) ? "))
c = int(input(" c (entier naturel) ? "))
d = int(input(" d (entier naturel) ? "))

"""     2ème partie -  CALCULS DES QTES DE MATIERES  -    """

# listes des variables
nA=[niA]
nB=[niB]
""" ICI !! coder l'instruction pour calculer la qté de matière de C """
""" ICI !! coder l'instruction pour calculer la qté de matière de D """
avancement=[0]  

x=0   # x : valeur incrémentée dans la boucle. Ne pas confondre avec la liste avancement[] 

""" ICI !! commenter les lignes suivantes avec # """
while nA[-1]>=0 and nB[-1]>=0:
    x=x+0.001    
    nA.append(niA-a*x)
    nB.append(niB-b*x)
    avancement.append(x)
""" ICI !! coder l'instruction pour calculer la qté de matière de C """
""" ICI !! coder l'instruction pour calculer la qté de matière de D """

"""     3ème partie -  L'ETAT FINAL  -    """

#la dernière itération doit etre effacée
""" ICI !! commenter la ligne suivante avec # """
del nA[-1]
del nB[-1]
""" ICI !! coder l'instruction pour calculer la qté de matière de C """
""" ICI !! coder l'instruction pour calculer la qté de matière de D """
del avancement[-1]

xmax=avancement[-1]

""" ICI !! commenter la ligne suivante avec # """
print(" xmax = {} mol".format(round(xmax,2)))
print(" qté de matière finale de A : {} mol".format(round(nA[-1],2)))
print(" qté de matière finale de B : {} mol".format(round(nB[-1],2)))
""" ICI !! coder l'instruction pour calculer la qté de matière de C """
""" ICI !! coder l'instruction pour calculer la qté de matière de D """


"""     4ème partie -  EVOLUTION DES QTES DE MATIERE  -    """

""" ICI !! commenter la ligne suivante avec # """
print("équation chimique: {} A + {} B = {} C + {} D".format(a,b,c,d))

""" ICI !! commenter la ligne suivante avec # """
plt.plot(avancement,nA,color="green",label="A")  
plt.plot(avancement,nB,color="red",label="B")
"""  ICI!! coder l'instruction pour tracer l'évolution de nC en blue """
"""  ICI!! coder l'instruction pour tracer l'évolution de nD en yellow"""

""" ICI !! commenter les lignes suivantes avec # """
plt.title("Evolution des qtés de matière")
plt.legend()
plt.xlabel("x (mol)")
"""  ICI!! coder l'instruction pour tracer la légende de l'axe des y"""

""" ICI !! commenter la ligne suivante avec # """
plt.show()