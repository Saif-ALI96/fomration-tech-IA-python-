
#  Nombres pairs

# my_liste = []
# for loop in range(1,10):
#     if loop % 2 == 0:
#         my_liste.append(loop)
    
# print(my_liste) 
# sortie des nombres paires ---> [2, 4, 6, 8]

liste_pairs = []
for pair in range(0,11,2):
    liste_pairs.append(pair)
print(liste_pairs)

#  une autre facon de le faire :

liste_pairs = [pair for pair in range(0,11,2)]


     
    
my_liste2 = []
for loop in range (1,10):
    if loop % 2 != 0 :
        my_liste2.append(loop)

print(my_liste2)
# sortie des nombres impaires ---> [1, 3, 5, 7, 9]

