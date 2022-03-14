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
# Inspitre du travaille de nacera
    elif niveaux == 3:

        nombre_de_tentative_nv3 = 1
        nombre_de_tentative_nv3_max = int(
            input("Choisissez le nombre d'essaie : "))
        prix_minimum = 1
        choix_prix_maximum = int(
            input("Choisissez un nombre maximum: "))
        prix = int(
            input(f"Entrer un nombre entre 1 et {choix_prix_maximum} : "))
        juste_prix = randint(prix_minimum, choix_prix_maximum)
        while juste_prix != prix and nombre_de_tentative_nv3 < nombre_de_tentative_nv3_max:
            if juste_prix < prix:
                print("c'est moin reessayer")
                print(
                    f"Vous avez utiliser {nombre_de_tentative_nv3} essai sur {nombre_de_tentative_nv3_max}\n")
                prix = int(
                    input(f"Entre nombre entre 1 et {choix_prix_maximum} : "))
            elif juste_prix > prix:
                print("c'est plus reessayer")
                print(
                    f"Vous avez utiliser {nombre_de_tentative_nv3} essai sur {nombre_de_tentative_nv3_max}")
                prix = int(
                    input(f"Entre nombre entre 1 et {choix_prix_maximum} : "))
            nombre_de_tentative_nv3 += 1
        else:
            if juste_prix != prix:
                print(" Il ne vous reste plus d'essai ")
                print(f" Vous avez perdu le bon nombre etait ({juste_prix})")

            else:
                print(
                    f"BRAVO le numero {juste_prix} est le numero gagnant,vous avez trouvé apres {nombre_de_tentative_nv3} essai de ce fait la parti est terminer au revoir au plaisir de vous revoir à tres bientôt.")
            exit
