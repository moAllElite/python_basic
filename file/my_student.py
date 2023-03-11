import datetime 
import operator
#student=[]
getAll=[]

allOut=[]
class Student:
    def __init__(self,matricule,name,date,moyenne):
        self.matricule=matricule;
        self.name=name;
        self.date=date;
        self.moyenne=moyenne
    """def showInfo(self,matricule,name,date,moyenne):
        print("\tle matricule client {0} ".format(self.matricule)
            +"\n\tle nom du client :",self.name
            +"\n\tla date est :"
        ,self.date   
        +"\nsa classe est :",self.moyenne
        )
    """
def saisirClient(student=[]):
    f=open("student.txt","w")
    matricule=int(input("entrer id:\t"))
    #student.append(matricule);
    name=input("entrer le nom du client:\t");
    #student.append(name);
    date=datetime.datetime.now().strftime("%A %m %Y");
    #student.append(date);
    moyenne=float(input("saisir la moyenne :\t"));
    #student.append(moyenne)
    result=f.write(str(matricule)+"\t"+name+"\t"+date+"\t"+str(moyenne))
    f.close()
def addClient():
    f=open("student.txt","a")
    matricule=int(input("entrer id:\t"))
    name=input("entrer le nom du client:\t")
    date=datetime.datetime.now().strftime("%A %m %Y")
    moyenne=float(input("saisir la moyenne :\t"))
    result=f.write(str(matricule)+"\t"+name+"\t"+date+"\t"+str(moyenne))
    f.close()
def showFile():
    f=open("student.txt","r")
    lists=f.read()
    lists=lists.replace("\t",",")
    print(lists.split(","))
    f.close()
def moyenneClass(sum=0):
    f=open("student.txt","r")
    lists=f.read()
    f.close()
    lists=lists.replace("\t",",")
    lists=lists.split(",")
    x=slice(3,len(lists),3)
    getAll=lists[x]
    for i in getAll:
        sum+=float(i)
        
    print("la moyenne de la classe vaut: \t", sum/len(getAll))