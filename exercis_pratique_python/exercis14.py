
#  14 Ajout d'éléments à une liste

L = []
nombres_entiers = [10,25,30,45,90 ,'ab','cd','ef']
L.extend(nombres_entiers)
# L.append("ab")
# L.append("cd")
L += nombres_entiers
print (L)

#  [10, 25, 30, 45, 90, 'ab', 'cd']