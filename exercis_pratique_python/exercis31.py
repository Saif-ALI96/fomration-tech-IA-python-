
#  Affichage de motifs 

#  Écrire un programme qui permet d'afficher sur la console les nombres 


# nombres = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# vraible = 0
# nouvelle_liste = []
# nouvelel_liste = nombres * vraible
# print(nouvelel_liste)
'''
for i in range(vraible):
    # print(i)
    nouvelle_liste.extend(nombres)
    # print(nouvelle_liste)
    if vraible > 0 :
        vraible += 1
    print(nouvelle_liste)
'''
'''
for _ in range(5,21):
    nouvelle_liste.append(_)
    print(nouvelle_liste)'''

nouvelle_liste = []

for x in range(5,21):
    for y in range(5):
        if x != y:
            nouvelle_liste.append((x,y))
print(nouvelle_liste)


# for j in range(8):
#     print(*[i for x in ])