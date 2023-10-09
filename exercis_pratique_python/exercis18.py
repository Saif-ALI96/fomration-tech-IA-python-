
#  Trier une liste de tuples 

l = [('Pomme',15),('Banane',8),('Fraise',12),('Kiwi',9),('Peche',2)]

liste_tri = sorted(l,key=lambda x:x[1])
print(liste_tri)

'''

1. Tout d'abord, vous avez une liste de tuples nommée `l`.
Chaque tuple contient deux éléments : le nom d'un fruit (une chaîne de caractères) et la quantité de ce fruit (un nombre entier). 
Par exemple, `('Pomme', 15)` signifie qu'il y a 15 pommes dans la liste.

2. Ensuite, vous utilisez la fonction `sorted()` pour trier la liste `l` en créant une nouvelle liste triée appelée `liste_tri`.

3. Dans `sorted()`, il y a un paramètre appelé `key`, qui permet de spécifier une fonction qui sera utilisée pour déterminer comment trier les éléments de la liste. 
Dans ce cas, vous utilisez une fonction lambda (une petite fonction anonyme) comme `lambda x: x[1]`.
- `lambda x: x[1]` signifie que pour chaque élément `x` (dans ce cas, un tuple), vous prenez le deuxième élément (`x[1]`) comme clé de tri.

4. Donc, `sorted()` parcourt chaque tuple de la liste `l` et trie les tuples en fonction du deuxième élément, c'est-à-dire la quantité de fruits. 
Les tuples seront triés du plus petit au plus grand en fonction de cette quantité.

5. Enfin, la liste triée `liste_tri` sera stockée dans cette variable.

'''