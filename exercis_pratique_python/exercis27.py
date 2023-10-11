
#  Écrire un programme qui permet de récupérer l'extension d'un ficher 

import os

chemin_ficher = "exercis27.py"

extension = os.path.splitext(chemin_ficher)

print(extension[1])  # sortie ---->  .py
print (type(extension)) # sortie ---> <class 'tuple'>

