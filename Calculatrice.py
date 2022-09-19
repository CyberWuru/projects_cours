nombre_un = ""

while not nombre_un.isdigit():
    nombre_un = input("Entrez le premier nombre: ")
    if not nombre_un.isdigit():
        print("Veuillez entrer un numéro valide")
    continue


nombre_deux = ""

while not nombre_deux.isdigit():
    nombre_deux = input("Entrez le deuxième numéro : ")
    if not nombre_deux.isdigit():
        print("Veuillez entrer un numéro valide")
    continue

result = int(nombre_un) + int(nombre_deux)

print(f"Le résultat de l'addition de {nombre_un} et de {nombre_deux} est de {result}")