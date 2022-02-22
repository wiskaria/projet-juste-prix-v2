from random import randint
print("Bonjour et bienvenue au juste prix")
prix = randint(1, 100)
tentative = 10
nombre_de_tentative = 0
reponse = int(
    input(f"Entrer un prix entre 1 et 100 vous avez {tentative} tentative : "))

while prix != reponse:
    tentative -= 1
    nombre_de_tentative = nombre_de_tentative+1
    print(f"Il vous reste {tentative}")
    if prix > reponse:
        print(f"Plus grande que {reponse}")
        reponse = int(input("Entrer un prix: "))
    else:
        print(f"Plus petit que {reponse}")
        reponse = int(input("Entrer un prix: "))
    if tentative == 1:
        print(f"Partie terminée la bonne réponse était {prix}")
        exit()
if prix == reponse:
    print(
        f"Bravo bien joué, il vous a fallu {nombre_de_tentative+1} pour touvez le juste prix est de {prix}")
