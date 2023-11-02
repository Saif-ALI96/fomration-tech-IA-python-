
#  Les valeurs d'un dictionnaire 

dict_fruits = {'Pomme':3 , 'Banane': 7, 'Kiwi':1}

cle_afficher = ['Pomme', 'Banane']
for i in cle_afficher:
    if i in dict_fruits:
        # 1- 
        # print(dict_fruits)  # ----> {'Pomme': 3, 'Banane': 7, 'Kiwi': 1} {'Pomme': 3, 'Banane': 7, 'Kiwi': 1}
        # il repete deux fois parce que la liste contient deux elements
        # 2- 
        # print(key) # ----> Pomme Banane , ca va afficher les deux cles 
        # 3-
        
        print(dict_fruits[i]) # ----> ca va afficher les valeurs de cles "Pomme" et "Banane" qui sont le 3 et 7
