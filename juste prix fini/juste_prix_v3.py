from pickle import TRUE
from random import randint
print("Bonjour et bienvenue au juste prix")

niveau = int(input("\nVeuillez choisir votre niveau de difficulté de 1 à 3 \n 1) Le mode facile choisiissez entre 1 et 100 sans limite d’essais\n2)Le mode normal choisiissez entre 1 et 100 en 10 essais\n3)Le mode personnalisé   "))


while TRUE:

    if niveau == 1:
        prix = randint(1, 100)
        reponse = int(
            input("Entrer un prix entre 1 et 100 : "))
        if prix > reponse:
            print(f"Plus grande que {reponse}")
            reponse = int(input("Entrer un prix: "))
        else:
            print(f"Plus petit que {reponse}")
            reponse = int(input("Entrer un prix: "))
        exit()
    elif niveau == 2:
        nombre_de_tentative = 0
        prix = randint(1, 100)
        reponse = int(
            input(f"Entrer un prix entre 1 et 100 vous avez 10 tentative : "))
        nombre_de_tentative = nombre_de_tentative+1
        print(f"Vous avez {nombre_de_tentative}/10 tentatives")
        if prix > reponse:
            print(f"Plus grande que {reponse}")
            reponse = int(input("Entrer un prix: "))
        else:
            print(f"Plus petit que {reponse}")
            reponse = int(input("Entrer un prix: "))
        if nombre_de_tentative == 10:
            print(f"Partie terminée la bonne réponse était {prix}")
        exit()
    elif niveau == 3:
        maxi_choi = int(input("Choisissez  maximal"))
        prix = randint(1, maxi_choi)
        reponse = int(
            input(f"Entrer un prix entre 1 et 100 vous avez 10 tentative : "))
        nombre_de_tentative =

        if prix > reponse:
            print(f"Plus grande que {reponse}")
            reponse = int(input("Entrer un prix: "))
        else:
            print(f"Plus petit que {reponse}")
            reponse = int(input("Entrer un prix: "))
        if nombre_de_tentative == 10:
            print(f"Partie terminée la bonne réponse était {prix}")
            exit()
if prix == reponse:
    print(
        f"Bravo bien joué, il vous a fallu {nombre_de_tentative+1} pour touvez le juste prix est de {prix}")  # le décalage est du à l'indentation automatique
