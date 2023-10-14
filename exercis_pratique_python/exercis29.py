
# Écrire un programme qui permet de mélanger aléatoirement les éléments d'une liste L:

import random

L = [3,6,8,7,2,'s','ch','d']
liste_aleatoire = random.shuffle(L)

print(L)

'''
La méthode shuffle () prend deux paramètres. Sur ces deux derniers, aléatoire est le paramètre facultatif. 
La séquence correspond à toute séquence que vous souhaitez mélanger. Elle peut être une liste, une chaîne ou un tuple.

L'argument optionnel random est la fonction qui renvoie un nombre flottant aléatoire compris entre 0,1 et 1,0. 
S'il n'est pas spécifié, alors par défaut, Python utilise la fonction random.random ().
'''


#  2. Mélangez une liste sans perdre la liste d'origine

Liste = [3,6,8,7,2,'s','ch','d','hi',10]

la_nouvelle_liste = Liste[:]

random.shuffle(la_nouvelle_liste)

print(f'la nouvelle liste est : {la_nouvelle_liste}')

print(f'la liste originale est : {Liste}')


