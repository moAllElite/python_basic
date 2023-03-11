from lib import * 
clients=[]
getAll=[]
class Client :
    def __init__(self,numero,name,date):
        self.numero=numero;
        self.name=name;
        self.date=date;
  
    def showInfo(self,numero,name,date):
        print("\tle numero client {0} ".format(self.numero)
            +"\n\tle nom du client :",self.name
            +"\n\tla date est :"
        ,self.date   )
def saisirClient(numero=0):
    numero+=1;
    clients.append(numero);
    name=input("entrer le nom du client:\t");
    clients.append(name);
    date=datetime.datetime.now().strftime("%A %m %Y");
    clients.append(date);
    return clients;