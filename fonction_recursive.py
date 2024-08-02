def factorielle(n):
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)
print(factorielle(7))

#initialise une variable resultà 1. Cela stockera la factorielle cumulative.
#Itération :  une forboucle parcourt les nombres de 1 à n. À chaque itération, le nombre actuel ( i) est multiplié par le resultet stocké dans result.
#Résultat de retour : une fois la boucle terminée, la fonction renvoie la valeur finale de result, qui est la factorielle calculée.