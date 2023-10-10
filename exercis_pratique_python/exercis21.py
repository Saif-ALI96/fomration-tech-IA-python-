

# Somme des valeurs d'un dictionnaire

dicte = {'Pomme':15,'Banane':8,'Fraise':12,'Kiwi':9 ,'Peche':2}

'''
total = 0
for i in dicte.values():
    total += i
    # print (total) 

print (total)
'''

#  avec la function sum()

total = sum(dicte.values())
print(total)
