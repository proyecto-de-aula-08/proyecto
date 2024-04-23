import tkinter as tk

#colores
fondo_entrar = "#3B93AA"
fondo_salir = "#3B93AA"
fondo_correcto = "#EBFAFE"
fondo_entrada= "#3B93AA"
invitado="#88A201"

# ventana
ventana = tk.Tk()
ventana.title("inicio de sesion")

ventana.geometry('645x600+400+50')
ventana.resizable(width=False, height=False)
fondo= tk.PhotoImage( file="1.png")
fondo1= tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

# varra para poder escribir
usuario = tk.StringVar()
password = tk.StringVar()

#entradas

entrada=tk.Entry(ventana, textvar=usuario, width=24, relief="flat",)
entrada.place(x=255, y=250)
entrada=tk.Entry(ventana, textvar=password, width=24, relief="flat",)
entrada.place(x=255, y= 415)

def salir():
    ventana.destroy()

# para salirse 
boton1 = tk.Button(ventana, text="salir", command=salir, cursor="hand2", bg= invitado, 
                  width=12, relief="flat", font=("comic Sans MS",15,"bold"))
boton1.place(x = 100, y = 490)


def ingresar():
    nombre = usuario.get
    contraseña = password.get

    if nombre == "emanuel" and contraseña == "1234":

        correcta()
    else:

        incorrecto()
    

 ## funcion correcta
def correcta():
    ventana.withdraw()
    window = tk.Toplevel()
    window.title("exito")
    window.geometry('645x600+400+50')
    window.resizable(width=False, height=False)
    fondo2= tk.PhotoImage(file="4.png")
    fondo3= tk.Label(window, image=fondo2).place(x=0, y=0, relwidth=1, relheight=1)
# botones de esta funcion
    boton3=tk.Button(window, text="continuar", cursor="hand2",width=14, relief="flat",bg=fondo_correcto,
                    font=("comic Sans MS",14,"bold"))
    boton3.place(x=240, y=340)

    window.mainloop()



    #funcion incorrecta
def incorrecto():
    ventana.withdraw()
    root= tk.Toplevel()
    root.title("problema")
    root.geometry('645x600+400+50')
    root.resizable(width=False, height=False)
    fondo= tk.PhotoImage(file="6.png")
    fondo1= tk.Label(root, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

    def regresar():
        root.withdraw()
        ventana.deiconify()


    boton4= tk.Button(root, text="intentar denuevo", command=regresar, cursor="hand2", width=14,
                      relief="flat", font=("comic Sans MS", 12, "bold"))
    boton4.place(x=240, y=340)




    root.mainloop()

boton2 = tk.Button(ventana, text="seguir", command= ingresar,cursor="hand2", bg= invitado, 
                  width=12, relief="flat", font=("comic Sans MS",15,"bold"))
boton2.place(x = 400, y = 490)



















tk.mainloop()