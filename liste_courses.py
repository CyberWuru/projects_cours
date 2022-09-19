import sys
import time

liste = []

MENU = """Veuillez faire votre choix parmi ces 5 options : 
===>
1 : Ajouter un article à la liste
2 : Retirer un article
3 : Consulter la liste
4 : Vider la liste
5 : Sortir 
"""

while True:
    choix = input("Veuillez faire votre choix : ")
    if choix not in MENU:
        print("Veuillez faire un choix valide...")
        continue

    if choix == "1":
        a_ajouter = input("Que voulez vous ajouter? ")
        liste.append(a_ajouter)
        print(f"{a_ajouter} a bien été ajouté/e à la liste")
        choix_deux = input("Souhaitez vous ajouter autre chose?")
        if choix_deux == "o" or "oui" or "OUI" or "Oui":
            a_ajouter_deux = input("Que suohaitez vous ajouter à la liste?")
            liste.append(a_ajouter_deux)
            print(f"{a_ajouter_deux} a bien été ajouté a votre liste")
        elif a_ajouter_deux == "n" or "no" or "non" or "NO" or "No" or "NON" or "Non":
            print("Très bien. Il n'y a rien a ajouter")
            print("Aurevoir et merci :)")
            continue
        else:
            print("Choix non valide!")
            print("Aurevoir")
            time.sleep(1)
            sys.exit()
        continue
    elif choix == "2":
        a_retirer = input("Que voulez vous retirer? ")
        if a_retirer not in liste:
            print("L'article que vous cherchez n'est pas dans la liste.")
        else:
            liste.remove(a_retirer)
            print(f"L'article {a_retirer} a bien été retiré de la liste")
        continue
    elif choix == "3":
        print("Voici votre liste actuelle : ")
        if not liste:
            print("Il n'a actuellement aucun article dans votre liste.")
        else:
            for i in enumerate(liste, 1):
                print(f"{i}")
        continue
    elif choix == "4":
        certain = input("Etes vous sur de votre choix? o/n ==> \n")
        if certain == "o":
            liste.clear()
            print("La liste a bien été vidée")
        elif certain == "n":
            print("Suppression annulée")
            continue
        continue
    elif choix == "5":
        print("Merci et aurevoir :) ")
        time.sleep(1)
        sys.exit()