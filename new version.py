import os
import getpass4
from validate_email import validate_email
def limpiar_pantalla():
    os.system('cls')




print("!Bienvenido¡")
print("1. Iniciar sesión")
print("2. Registrarse")
print("3. Salir")


opcion = int(input("Escoge una opción: "))

usuarios={}
# funcion para validar los correos electronicos
def verificar_correo(correo):
    return validate_email(correo)

#menú principal 
def menu_principal():
     while True:
         print("!Bienvenido al menú principal")
         print("")
         print("¿Que tipo de desecho deseas convertir a dinero?")
         print("")
         print("1. Plástico")
         print("2. Hierro")
         print("3. Cobre")
         print("4. Salir")

         opc=int(input("¿Cual desecho tienes?: "))
         if opc==1:
             print("Plástico")
             print("")    
             print("¿Cuantos kilogramos de plástico tienes")
             kg=float(input(": "))

             total = kg*300 
             limpiar_pantalla()

             print("!Esta es tu ganancia¡: ",total)
         elif opc==2:
             print("Hierro") 
             print("")
             print("¿Cuantos kilogramos de hierro tienes?")
             kg=float(input(": "))

             total=kg*1000 

             print("!Esta es tu ganancia¡: ", total)
         elif opc==3:
             print("Cobre")
             print("")
             print("¿Cuantos kilogramos de cobre tienes?")
             kg=float(input(": "))
             total=kg*10000
             print("!Esta es tu ganancia¡: ", total)
         elif opc==4:
             limpiar_pantalla()

             break
             
         
         else:
             opc=int(input("Ha ocurrido un error, intentalo de nuevo: "))

             
             

                   
        




# funcion para registrarse 
def registrarse():
    nombre = input("Ingresa tu correo electrónico: ")
    if nombre in usuarios:
        print("El correo ya existe, por favor elija otro correo")
        return

    # Verificar si el correo es válido
    if not verificar_correo(nombre):
        print("Correo electrónico no válido. Por favor, ingrese un correo válido.")
        return

    contraseña = getpass4.getpass("Ingresa tu contraseña: ")
    usuarios[nombre] = contraseña
    print("Registrado exitosamente")
    limpiar_pantalla()



# funcion para iniciar sesion 
def inicio_sesion():
    nombre = input("Ingresa tu correo electrónico: ")
    contraseña = getpass4.getpass("Ingresa tu contraseña: ")
    if nombre in usuarios and usuarios[nombre] == contraseña:
        print("Inicio de sesión exitoso")
        print("")
        limpiar_pantalla()
        # aqui incluimos la funcion de menu principal ya que antes aunque fallara el correo entraba, pero ahora
        # el correo y contraseña deben coinsidir con el registrado para poder acceder al menu principal
        print("Recicla tu dinero")
        menu_principal()
    else:
        print("Usuario o contraseña incorrecta. Intente de nuevo.")



# aqui se ejecuta todo el codigo, osea las funciones y diccionarios.
while True:
    if opcion ==1:
        inicio_sesion()
        # al finalizar el contenido de esta funcion 


        # se ejecutara el siguiente codigo
        print("!Bienvenido¡")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = int(input("Escoge una opción: "))
        
    elif opcion ==2:
        print("!Bienvenido al registro de usuario¡")
        registrarse()
        print("Registrado exitosamente")
        print("")
        print("!Bienvenido¡")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir") 
        print("")
        print("Ya puedes iniciar sesión")

        opcion =int(input("Escoge una opción"))


    elif opcion==3:
        print("Adiós.")
        break
    else:
        print("Opcion incorrecta")
        print("")
        print("!Bienvenido¡")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")


        opcion = int(input("Escoge de nuevo la opción: "))
        
