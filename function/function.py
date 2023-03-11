from lib import *
choix=0
while(choix!=6):
    print("\n\t\t*******Caltulatrice*******\t\t")
    print("\t\t1-Saisir les 2 entiers\n")
    print("\t\t2-Calcul de la somme\n")
    print("\t\t3-Calcul de la difference\n ")
    print("\t\t4-Calcul de la multiplication\n")
    print("\t\t5-Calcul de la division\n")
    print("\t\t6-Table de multiplication\n ")
    print("\t\t7-Exit\n")
    choix=int(input("Faites votre choix :\t"))
    if(choix==1):
        x=int(input("saisir la  1ere valeur entier :")) ;
        y=int(input("saisir la 2eme valeur entiere :"));
        while (x<=0 or y<=0 ):
            if(x<=0):
                 x=int(input("saisir la  1ere valeur entier :")) ;
            else :
                y=int(input("saisir la 2eme valeur entiere :"));
        
    elif(choix==2):
            print("la somme vaut  entre {0} et {1} vaut :".format(x,y),somme(x,y));
    
    elif(choix==3):
        print("la difference  entre {0} et {1} vaut :".format(x,y),minus(x,y));
    
    elif(choix==4):
        print("la difference  entre {0} et {1} vaut :".format(x,y),multiple(x,y));
    elif(choix==5):
        print("la division  entre {0} et {1} vaut :".format(x,y),
        float( divide(x,y)));
    elif (choix==6):  
        o=int(saisiDeNombrePositif());
        print(tableMultiplication());
    elif(choix==7):
        print("Bonne journee",datetime.datetime.now().strftime("%A %M %Y"));
        break;
  
    else:
        print("le choix est compris entre 1 et 5");
    
           

