import libModule
def sayHello(name):
    print("hello \t"+name)

def square(x):
    print("\nle carre de {0} vaut:".format(x),libModule.math.pow(x,2))