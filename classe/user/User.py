list=[]
class User:
    def __init__(self,nomComplet,age):
        self.nomComplet=nomComplet;
        self.age=age;
    def message(self,age):
        if(age<18):
            print("i'm {0} , i'm not average".format(self.age))
        else:
            print("i'm {0} ,i'm average".format(self.age))
    
def saisiUser():
    a=input("Entrer le nom du user:\t")
    b=int(input("Entrer l'age du user:\t"))
    while(b<=0):
        b=int(input("Entrer l'age du user:\t")) 
    list.append(a);
    list.append(b);
    return list
def affichage():
    user=User(list[0],list[1])
    print("\t\tle nom est : {0} \nl'age vaut:\t{1}" .format(user.nomComplet,user.age))
    user.message(user.age);

    