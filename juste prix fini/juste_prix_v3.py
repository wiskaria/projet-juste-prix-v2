#  désoler je n'est pas put finir a temps


from pickle import TRUE
from random import randint
print("Bonjour et bienvenue au juste prix")


while TRUE:
    niveau = int(input("\nVeuillez choisir votre niveau de difficulté de 1 à 3 \n 1) Le mode facile choisiissez entre 1 et 100 sans limite d’essais\n2)Le mode normal choisiissez entre 1 et 100 en 10 essais\n3)Le mode personnalisé \n niveau :   "))
    niveaux = niveau
    if niveaux == 1:
        prix = randint(1, 100)
        tentative_nv_1 = 0
        reponse = int(
            input("Entrer un prix entre 1 et 100 : "))

        while reponse != prix:
            tentative_nv_1 = tentative_nv_1+1
            if prix > reponse:
                print(f"Plus grande que {reponse}")
                reponse = int(input("Entrer un prix: "))
            else:
                print(f"Plus petit que {reponse}")
                reponse = int(input("Entrer un prix: "))
        if prix == reponse:
            print(
                f"Bravo bien joué, il vous a fallu {tentative_nv_1+1} de tentatives pour touvez le juste prix est de {prix}")
            exit()
    elif niveaux == 2:
        prix_nv2 = randint(1, 100)
        nombre_de_tentative_nv2 = 0
        reponse_nv2 = int(
            input(f"Entrer un prix entre 1 et 100 vous avez 10 tentative : "))

        while reponse_nv2 != prix_nv2 and nombre_de_tentative_nv2 < 10:
            nombre_de_tentative_nv2 = nombre_de_tentative_nv2+1
            print(f"Vous avez {nombre_de_tentative_nv2}/10 tentatives")

            if prix_nv2 > reponse_nv2:
                print(f"Plus grande que {reponse_nv2}")
                reponse_nv2 = int(input("Entrer un prix: "))

            elif prix_nv2 < reponse_nv2:
                print(f"Plus petit que {reponse_nv2}")
                reponse_nv2 = int(input("Entrer un prix: "))

        if prix_nv2 == reponse_nv2:
            print(
                f"Bravo bien joué, il vous a fallu {nombre_de_tentative_nv2+1} pour touvez le juste prix est de {prix_nv2}")
        elif nombre_de_tentative_nv2 == 10:
            print(f"Partie terminée la bonne réponse était {prix_nv2}")
            exit()
    elif niveaux == 3:
        maxi_choi = int(
            input("Choisissez le prix maximal le minimome est 1 : "))
        prix_nv3 = randint(1, maxi_choi)
        nombre_de_tentative = int(input("Entre un nombre de tentative :  "))
        reponse_nv3 = int(
            input(f"Entrer un prix entre 1 et {maxi_choi} vous avez 10 tentative : "))
        tentative = nombre_de_tentative
        while nombre_de_tentative != tentative and reponse_nv3 != prix_nv3:
            tentative = tentative-1
            if prix_nv3 > reponse_nv3:
                print(f"Plus grande que {reponse_nv3}")
                reponse_nv3 = int(input("Entrer un prix: "))
            else:
                print(f"Plus petit que {reponse_nv3}")
                reponse_nv3 = int(input("Entrer un prix: "))
        if prix_nv3 == reponse_nv3:
            print(
                f"Bravo bien joué, il vous a fallu {nombre_de_tentative+1} pour touvez le juste prix est de {prix_nv3}")
        if tentative == 0:
            print(f"Partie terminée la bonne réponse était {prix_nv3}")
