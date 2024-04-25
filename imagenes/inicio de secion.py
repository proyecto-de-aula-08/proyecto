# biblioteca usada o modulo jajaja no se solo se que sirve :)
import tkinter as tk

#colores para cada boton

invitado="#88A201"
fondo_correcto = "#EBFAFE"
boton_1="#3B93AA"


#ventana principal
ventana = tk.Tk()
ventana.title("inicio")
ventana.geometry('500x500+500+60')
ventana.resizable(width=False, height=False)

fondo = tk.PhotoImage(file="2.png")
fondo1=tk.Label(ventana, image=fondo).place(x=0, y=0, relheight=1, relwidth=1)

       
# funcion para registrarse
def registro():
    ventana.withdraw()
    window = tk.Toplevel()
    window.title("registro")
    window.geometry('500x500+500+60')
    window.resizable(width=False, height=False)
    #fondo de esta ventana
    fondo = tk.PhotoImage(file="5.png")
    fondo1 = tk.Label(window, image=fondo).place(x=0, y=0, relheight=1, relwidth=1)

    #boton para continuar
    boton = tk.Button(window, text="continuar",command=inicio, relief="flat", cursor="hand2",bg=invitado,
                      width=12, font=("comic Sans MS",15,"bold"))
    boton.place(x=195, y=450)
    # barras para escrivir
    correo = tk.StringVar()
    contraseña = tk.StringVar()
    edad= tk.StringVar()
    #entrada de texto
    entrada= tk.Entry(window, textvar=correo,width=22, relief="flat")
    entrada.place (x= 200, y=168)
    entrada= tk.Entry(window, textvar=contraseña,width=22, relief="flat")
    entrada.place (x= 200, y=278)
    entrada= tk.Entry(window, textvar=edad,width=22, relief="flat")
    entrada.place (x= 200, y=395)

    # ejecicion de esta ventana
    window.mainloop()

 
# funcion para inicio de sesion
def inicio():
    ventana.withdraw()
    root= tk.Toplevel()
    root.title("inisio de sesion")
    root.geometry('500x500+500+50')
    root.resizable(width=False, height=False)
    # fondo de esta ventana
    fondo = tk.PhotoImage(file="1.png")
    fondo1=tk.Label(root, image=fondo).place(x=0, y=0, relheight=1, relwidth=1)

    def regresar():
        root.withdraw()
        ventana.deiconify()
    # boton para regresar
    boton= tk.Button(root, text="regresar", width=12,command=regresar, relief="flat", cursor="hand2",bg=invitado ,
                     font=("comic Sans MS",15,"bold"))
    boton.place(x=35, y=430)
    # barras para escrivir
    correo= tk.StringVar()
    contraseña= tk.StringVar()

    # entrada de texto
    entrada = tk.Entry(root, textvar=correo, width=35, relief="flat")
    entrada.place(x=140, y= 200)
    entrada = tk.Entry(root, textvar=contraseña, width=35, relief="flat")
    entrada.place(x=140, y= 378)

    #ejecucion de la ventana
    root.mainloop()



# botones
# iniciar sesion
boton1 = tk.Button(ventana, text="Iniciar sesión",command=inicio, cursor="hand2", bg= boton_1, 
                  width=12, relief="flat", font=("comic Sans MS",15,"bold"))
boton1.place(x = 190, y = 156)
# registrarse    
boton2 = tk.Button(ventana, text="Registrarse",command=registro, cursor="hand2", bg= boton_1, 
                  width=12, relief="flat", font=("comic Sans MS",15,"bold"))
boton2.place(x = 190, y = 290)

# ejecicion de la ventana principal
ventana.mainloop()
