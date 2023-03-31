#Exercice pair ou impair
#Créez un programme qui permet de déterminer si l'argument donné est un entier pair ou impair.

def  entier(l):
    pair = []
    impair = []
    for i in l :
        if (i%2 == 0):
            pair.append(i)
        else:
            impair.append(i)
    print("Nombre pair : ", pair)
    print("Nombre impair :", impair)

l = [43, 3, 49, 92, 72, 487, 28, 908, 873, 22, 34]
print(entier(l))
