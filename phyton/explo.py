print("1. suma")
print("2.resta")
print("3.multiplicasion")
print("4. division")
print("5. potencia")
x = int(input("que opcion escoges: "))

while x != 0:
    if x != 1 and x!=2 and x!=3 and x!=4 and x!=5:
        print("opcion no valida.")
        print("1. suma")
        print("2.resta")
        print("3.multiplicacion")
        print("4. division")
        print("5. potencia")
        x  = int(input("dame un numero: "))
#primera parte suma
    elif x==1:
        print("suma.")
        x = int(input("dame el primer numero: "))
        y= int(input("dame el segundo numero: "))
        if x<0:
            print("error")
            print("suma.")
            x = int(input("dame el primer numero: "))
            y= int(input("dame el segundo numero: "))
            suma = x+y
            print("esta es tu suma",suma)
        suma = x+y
        print("esta es tu suma",suma)
        a=int(input("1. para salir, 2. para sumar otro numero"))
        if a == 1:
            print("1. suma")
            print("2.resta")
            print("3.multiplicasion")
            print("4. division")
            print("5. potencia")
            x = int(input("que opcion escoges: "))
        elif a==2:
            print("suma.")
        x = int(input("dame el primer numero: "))
        y= int(input("dame el segundo numero: "))
        suma = x+y
        print("esta es tu suma",suma)
        a=int(input("1. para salir, 2. para sumar otro numero"))
        break   
#segund parte resta
    elif x == 2:
        print("resta.")
        x = int(input("dame el primer numero: "))
        y= int(input("dame el segundo numero: "))
        resta = x-y
        print("esta es tu resta.",resta)
#tercera parte multiplicacion
    elif x == 3:
        print("multiplicacion.")
        x = int(input("dame un numero: "))
        y = int(input("dame el segundo numero: "))
        multiplicasion = x * y
        print("este es el resultado.",multiplicasion)
#cuarta parte division 
    elif x == 4:
        print("division.")
        x=int(input("dame el primer numero: "))
        y=int(input("dame el segundo numero: "))
        division = x/y
        modulo= x%y
        print("esta es tu division",division,"y este es su modulo",modulo)
#quinta parte potencia 
    elif x == 5:
        print("potencia.")
        x=int(input("dame el numero: "))
        y=int(input("dame la potencia: "))
        potencia=x**y
        print("esta es su potencia.",potencia)
    