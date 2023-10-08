
#  Trier une liste
'''
Pour ordonner une liste de manière croissante en Python, vous pouvez utiliser :
la méthode sort() pour trier la liste directement sur place (c'est-à-dire que la liste d'origine sera modifiée),
ou vous pouvez utiliser la fonction sorted() pour créer une nouvelle liste triée sans modifier la liste d'origine. `

'''

my_liste = [6,8,3,4,1,12,2,9,2]
my_liste.sort()
print(my_liste) 
#  tri d'une ordre croissant[1, 2, 2, 3, 4, 6, 8, 9]


my_liste2=[50,-7, -1]

my_liste_tri = sorted(my_liste2) # sorted est une fonction qui permet de trier un tableau en utilisant
print (my_liste2)# l'ordre croissant par défaut


'''

Pour trier une liste de manière décroissante en Python, vous pouvez utiliser :
la méthode sort() avec l'argument reverse=True pour trier la liste directement sur place en ordre décroissant,
ou vous pouvez utiliser la fonction sorted() avec l'argument reverse=True pour créer une nouvelle liste triée de manière décroissante sans modifier la liste d'origine. 
Voici comment faire les deux :
'''

# tri la liste d'une facone descroissant
ma_liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

ma_liste.sort(reverse=True)  # Trie la liste sur place en ordre décroissant
print(ma_liste)
#[9, 6, 5, 5, 5, 4, 3, 3, 2, 1,



ma_liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

liste_triee = sorted(ma_liste, reverse=True)  # Crée une nouvelle liste triée en ordre décroissant sans modifier l'originale
print(liste_triee)
