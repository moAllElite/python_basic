from my_student import *
choix=1
while(choix!=5):
    print("\n\t\t\t\t****Menu****\t\t\t")
    print("\t\t\t1-saisir les informations de l'eleve")
    print("\t\t\t2-Affichage du fichier")
    print("\t\t\t3-Ajouter une  eleve")
    print("\t\t\t4-Calcul de la moyenne de la classe")
    print("\t\t\t5-Exit")
    choix=int(input("faites votre choix :\t"))
    if(choix==1):
        saisirClient()
    elif(choix==2):
        showFile()
    elif(choix==3):
            addClient()
    elif(choix==4):
        moyenneClass()
    elif (choix==5):
        print("bye bye!!!")
    else:
        print("votre choix doit être entre 1 et 4")