from Client import *
from lib import *
choix=0
while(choix!=3):
    print("\n\t\t\t****Menu****\t\t\t\t")
    print("\t\t1-Saisir le nom complet \n")
    #print("\t\t2-Saisir age du user\n")
    print("\t\t2-Affichage des infos\n")
    print("\t\t3-Exit\n")
    choix=int(input("Faites votre choix:\t"))
    if(choix==1):
        saisirClient() ; 
        client=Client(clients[0],clients[1],clients[2])
    elif(choix==2):
            client.showInfo(client.numero,client.name,client.date);
    elif(choix==3):
        print("by by!!!")
    else:
        print("le choix est compris entre 1 et 3")