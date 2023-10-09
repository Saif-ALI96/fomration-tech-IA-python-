
#  Éléments en commun entre deux listes

l1 = [9,8,7,14,3,2,'a','p','bonjour','b']
l2 = ['b', 1,9.2,6,3,9,'p']

#  ici on va transferer la liste en set()

set_l1 = set(l1)
set_l2 = set(l2)

# ici on va trouver les elements en commun entre les deux listes 

elements_en_commun = set_l1 & set_l2

#  list() , c'est une function de liste qui transfere le set en liste 

l3 = list(elements_en_commun)

print (l3)
#  sortie -----> [9, 3, 'p', 'b']

# l3 = [elements_en_commun] ---- > ici il va mettre les elements en commun dans le set et les inserer dans une liste 
#  qu'on aura la sortie suivante ----> [{'b', 9, 3, 'p'}]

