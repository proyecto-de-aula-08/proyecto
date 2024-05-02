# recilando tu dinero 

print("!Bienvenido¡")
print("1. Iniciar sesion")
print("2. Registrarce")
print("3. Salir")

opcion = int(input("Escoge una opcion: "))

# esto gurdara todos los datos
usuarios={}

# funcion para registrarce

def registrarse():
    nombre = input("Ingresa tu correo electronico: ")
    if nombre in usuarios:
        print("El correo ya existe, por favor elija otro correo")
        return
    contraseña = input("Ingresa tu contraseña: ")
    usuarios[nombre]= contraseña
    print("Registrado exitosamente")

# funcion para iniciar sesion 
def inicio_sesion():
    nombre = input("Ingresa tu correo electronico: ")
    contraseña = input("Ingresa tu contraseña: ")
    if nombre in usuarios and usuarios[nombre] == contraseña:
        print("Inicio de sesion exitoso")
    else:
        print("Usuario o contraseña incorrecta. Intente de nuevo.")
   
# while True para mantenerlo siempre activo 
while True:
    if opcion > 3 or opcion <= 0:
        print("Opcion incorrecta")

        print("BIENVENIDO AL MENU DE INICIO")
        print("1. Iniciar sesion")
        print("2. Registrarse")
        print("3. Salir")
        opcion = int(input("Elige de nuevo: "))
    elif opcion == 2:
        print("Bienvenido al registro de usuario")
        registrarse()
        print("BIENVENIDO AL MENU DE INICIO")
        print("1. Iniciar sesion")
        print("2. Registrarse")
        print("3. Salir")
        opcion = int(input("Escoge una opcion: "))
    elif opcion == 3:
       print("Saliendo.")
       break
        
    elif opcion == 1:
        print("Bienvenido al inicio de sesion")
        inicio_sesion()
        print("1. para continuar al menu pricipal , 2. regresar")
        opcion = int(input(": "))
        if opcion == 1:
            while True:
                if opcion ==1:
                   
                  print("Menu Principal")
                  print("")
                  print("1. plasticos")
                  print("2. Hierro")
                  print("3. cobre")
                  print("4. salir")
                  opcion = int(input("Escoge una opcion: "))

                  if opcion == 1:
                   print("cuantos kilogramos de plastico tienes")
                   kilogramos = float(input(": "))

                   pesos = kilogramos * 300
                   print("Esta es tu ganancia.", pesos)
                   opc= int(input("1. regresar"))
                   if opc==1:
                     print("Menu Principal")
                     print("")
                     print("1. plasticos")
                     print("2. Hierro")
                     print("3. cobre")
                     print("4. salir")
                     opcion = int(input("Escoge una opcion: "))

                elif opcion == 2:
                   print("Cuantos kilogramos de hierro tienes.")
                   kg= float(input(": "))
                   pesos= kg * 1000
                   print("esta es tu ganancia.", pesos)
                   opc= int(input("1. regresar"))

                   if opc==1:
                    print("Menu Principal")
                    print("")
                    print("1. plasticos")
                    print("2. Hierro")
                    print("3. cobre")
                    print("4. salir")
                    opcion = int(input("Escoge una opcion: "))

                elif opcion == 3:
                   print("cuantos kilogramos de cobre tienes")
                   kg = float(input(": "))
                   pesos = kg * 10000
                   print("esta es tu ganancia", pesos)
                   opc= int(input("1. regresar"))
                   if opc==1:
                    print("Menu Principal")
                    print("")
                    print("1. plasticos")
                    print("2. Hierro")
                    print("3. cobre")
                    print("4. salir")
                    opcion = int(input("Escoge una opcion: "))
                elif opcion == 4:
                   print("Adios.")
                   break 
        elif opcion ==2:
           print("!Bienvenido¡")
           print("1. Iniciar sesion")
           print("2. Registrarce")
           print("3. Salir")

           opcion = int(input("Escoge una opcion: "))
           
        

