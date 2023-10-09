
#  Liste de compréhension 
'''
liste = [1,2,3,4,5,6,7,8,9,10]
liste1 = []

for i in liste:
    range(liste1[i] + 2)
print(i)
    '''
liste = [1,2,3,4,5,6,7,8,9,10]
l2 = []

for nombres in liste[::2]:
    l2.append(nombres)
    
print (l2)
#  sortie ----> [1, 3, 5, 7, 9]