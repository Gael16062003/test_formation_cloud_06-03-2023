import datetime

def enregistrer_personne():
    nom = input("Entrez un nom : ")
    prenom = input("Entrez un prénom : ")
    email = input("Entrez un email : ")
    numéro = input("Entrez votre numéro : ")

    # Obtenir la date du jour
    today = datetime.datetime.now()
    today_x= today.strftime("%d/%m/%y")


    # Écrire les informations dans le fichier
    with open('enregistrement.txt', 'a') as f:
        f.write('Nom : ' + nom + ', Prénom : ' + prenom + ', Email : ' + email + ', Numéro : ' + numéro + ', Date  : ' + str(today_x) + '\n')
        print('Enregistrement effectué avec succès.')

def afficher_liste_enregistrement():
    with open('enregistrement.txt', 'r') as f:
        for ligne in f:
            print(ligne)

def rechercher_enregistrement_par_date():
    date_recherchee = input("Entrez une date à rechercher NB:pour l'année( 2023=23 )(format JJ/MM/AA) : ")

    with open('enregistrement.txt', 'r') as f:
        for ligne in f:
            if date_recherchee in ligne:
                print(ligne)
            else:
                print("la date entrée n'exite pas dans les archives")


# Afficher un menu et effectuer une action en fonction du choix
while True:
    print('1. Enregistrer une personne')
    print('2. Afficher la liste d\'enregistrement')
    print('3. Rechercher un enregistrement par date')
    print('4. Quitter')
    choix = input('Entrez votre choix : ')

    if choix == '1':
        enregistrer_personne()
    elif choix == '2':
        afficher_liste_enregistrement()
    elif choix == '3':
        rechercher_enregistrement_par_date()
    elif choix == '4':
        break
    else:
        print('Choix non valide.')


