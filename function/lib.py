import datetime
#calculatrice
def somme(a,b):
    return  a+b

def minus(a,b):
    return a-b

def multiple(a,b):
    return a*b

def divide(a,b):
    return a/b

def saisiDeNombrePositif():
    x=int(input("entrer un nombre positif :\t"))
    while (x<=0):
          x=int(input("entrer un nombre positif:\t"))
    
def tableMultiplication(a,i):
   
    while(i<11):
        print(a,"*",i,"=",i*a)
        i+=1
        
    
    
