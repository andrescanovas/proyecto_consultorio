from tkinter import *
from crearsb import *

def turnos():
    """Esta funcion sirve para crear una ventana emergente en la cual se mostraran los campos para generar turnos"""

    new_window = Toplevel()
    new_window.title("Turnos")




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






    Boton1 = Button(new_window, text='Enviar')
    Boton1.grid(row = 20,column = 4, sticky="e",padx=5,pady=5 )

    Boton1 = Button(new_window, text='Cancelar',command=new_window.destroy)
    Boton1.grid(row = 20,column = 5, sticky="e",padx=5,pady=5 )

    




    new_window.mainloop()