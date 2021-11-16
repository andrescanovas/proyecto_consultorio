from tkinter import *
from crearsb import *

def alta_de_medico():
    """Esta funcion sirve para crear una ventana emergente en la cual se mostraran los campos para dar de alta un paciente y no requiere ingresar datos en la funcion"""

    new_window = Toplevel()
    new_window.title("Registro de medico")




    lblnombre = Label(new_window, text="Nombre")
    lblnombre.grid(row=0, column=0, sticky="e", padx=5, pady=5)								
    nombre= StringVar()
    ntrnombre = Entry(new_window,textvariable=nombre)
    ntrnombre.grid(row=0, column=1, padx=5, pady=5)                 

    lblapellido = Label(new_window, text="Apellido")
    lblapellido.grid(row=0, column=2, sticky="e", padx=5, pady=5)						
    apellido= StringVar()
    ntrapellido = Entry(new_window,textvariable=apellido)
    ntrapellido.grid(row=0, column=3, padx=5, pady=5)

    lbledad = Label(new_window, text="Edad")
    lbledad.grid(row = 0, column = 4, sticky="e", padx=5,pady=5)
    edad = IntVar()
    ntredad = Entry(new_window,textvariable=edad)
    ntredad.grid(row = 0,column = 5, sticky="e",padx=5,pady=5 )

    lbldni = Label(new_window, text="DNI")
    lbldni.grid(row=1, column=0, sticky="e", padx=5, pady=5)						
    dni= StringVar()
    ntrdni = Entry(new_window,textvariable=dni)
    ntrdni.grid(row=1, column=1, padx=5, pady=5) 


    lbltelefono = Label(new_window, text="Telefono")
    lbltelefono.grid(row=2, column=0, sticky="e", padx=5, pady=5)						
    telefono= StringVar()
    ntrtelefono = Entry(new_window,textvariable=telefono)
    ntrtelefono.grid(row=2, column=1, padx=5, pady=5)

    lblemail = Label(new_window, text="eMail")
    lblemail.grid(row=2, column=2, sticky="e", padx=5, pady=5)						
    email= StringVar()
    ntremail = Entry(new_window,textvariable=email)
    ntremail.grid(row=2, column=3, padx=5, pady=5)

    lblcalle = Label(new_window, text="Calle")
    lblcalle.grid(row=3, column=0, sticky="e", padx=5, pady=5)						
    calle= StringVar()
    ntrcalle = Entry(new_window,textvariable=calle)
    ntrcalle.grid(row=3, column=1, padx=5, pady=5)

    lblaltura = Label(new_window, text="Altura")
    lblaltura.grid(row=3, column=2, sticky="e", padx=5, pady=5)						
    altura= StringVar()
    ntraltura = Entry(new_window,textvariable=altura)
    ntraltura.grid(row=3, column=3, padx=5, pady=5)

    lblciudad = Label(new_window, text="Ciudad")
    lblciudad.grid(row=4, column=0, sticky="e", padx=5, pady=5)						
    ciudad= StringVar()
    ntrciudad = Entry(new_window,textvariable=ciudad)
    ntrciudad.grid(row=4, column=1, padx=5, pady=5)

    lblprovincia = Label(new_window, text="Provincia")
    lblprovincia.grid(row=4, column=2, sticky="e", padx=5, pady=5)						
    provincia= StringVar()
    ntrprovincia = Entry(new_window,textvariable=provincia)
    ntrprovincia.grid(row=4, column=3, padx=5, pady=5)

    lblpais = Label(new_window, text="Pais")
    lblpais.grid(row=4, column=4, sticky="e", padx=5, pady=5)						
    pais= StringVar()
    ntrpais = Entry(new_window,textvariable=pais)
    ntrpais.grid(row=4, column=5, padx=5, pady=5)

    lblmedicoCabe = Label(new_window, text="MEDICO CABECERA")
    lblmedicoCabe.grid(row=4, column=6, sticky="e", padx=5, pady=5)						
    medicoCabe= StringVar()
    ntrlblmedicoCabe = Entry(new_window,textvariable=lblmedicoCabe)
    ntrlblmedicoCabe.grid(row=4, column=7, padx=5, pady=5)




    Boton1 = Button(new_window, text='Enviar', command=lambda:guardar_datos_de_medicos(nombre,apellido,edad,dni,telefono,email,calle,altura,ciudad,provincia,pais,medicoCabe))
    Boton1.grid(row = 20,column = 4, sticky="e",padx=5,pady=5 )

    Boton1 = Button(new_window, text='Cancelar',command=new_window.destroy)
    Boton1.grid(row = 20,column = 5, sticky="e",padx=5,pady=5 )

    




    new_window.mainloop()