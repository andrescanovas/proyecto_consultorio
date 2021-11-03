from tkinter import *
from crearsb import *

root = Tk()
root.title("Formulario de ingreso")




lblnombre = Label(root, text="Nombre")
lblnombre.grid(row=0, column=0, sticky="e", padx=5, pady=5)								
nombre= StringVar()
ntrnombre = Entry(root,textvariable=nombre)
ntrnombre.grid(row=0, column=1, padx=5, pady=5)                 

lblapellido = Label(root, text="Apellido")
lblapellido.grid(row=0, column=2, sticky="e", padx=5, pady=5)						
apellido= StringVar()
ntrapellido = Entry(root,textvariable=apellido)
ntrapellido.grid(row=0, column=3, padx=5, pady=5)

lbledad = Label(root, text="Edad")
lbledad.grid(row = 0, column = 4, sticky="e", padx=5,pady=5)
edad = IntVar()
ntredad = Entry(root,textvariable=edad)
ntredad.grid(row = 0,column = 5, sticky="e",padx=5,pady=5 )

lbldni = Label(root, text="DNI")
lbldni.grid(row=1, column=0, sticky="e", padx=5, pady=5)						
dni= StringVar()
ntrdni = Entry(root,textvariable=dni)
ntrdni.grid(row=1, column=1, padx=5, pady=5) 


lbltelefono = Label(root, text="Telefono")
lbltelefono.grid(row=2, column=0, sticky="e", padx=5, pady=5)						
telefono= StringVar()
ntrtelefono = Entry(root,textvariable=telefono)
ntrtelefono.grid(row=2, column=1, padx=5, pady=5)

lblemail = Label(root, text="eMail")
lblemail.grid(row=2, column=2, sticky="e", padx=5, pady=5)						
email= StringVar()
ntremail = Entry(root,textvariable=email)
ntremail.grid(row=2, column=3, padx=5, pady=5)

lblcalle = Label(root, text="Calle")
lblcalle.grid(row=3, column=0, sticky="e", padx=5, pady=5)						
calle= StringVar()
ntrcalle = Entry(root,textvariable=calle)
ntrcalle.grid(row=3, column=1, padx=5, pady=5)

lblaltura = Label(root, text="Altura")
lblaltura.grid(row=3, column=2, sticky="e", padx=5, pady=5)						
altura= StringVar()
ntraltura = Entry(root,textvariable=altura)
ntraltura.grid(row=3, column=3, padx=5, pady=5)

lblciudad = Label(root, text="Ciudad")
lblciudad.grid(row=4, column=0, sticky="e", padx=5, pady=5)						
ciudad= StringVar()
ntrciudad = Entry(root,textvariable=ciudad)
ntrciudad.grid(row=4, column=1, padx=5, pady=5)

lblprovincia = Label(root, text="Provincia")
lblprovincia.grid(row=4, column=2, sticky="e", padx=5, pady=5)						
provincia= StringVar()
ntrprovincia = Entry(root,textvariable=provincia)
ntrprovincia.grid(row=4, column=3, padx=5, pady=5)

lblpais = Label(root, text="Pais")
lblpais.grid(row=4, column=4, sticky="e", padx=5, pady=5)						
pais= StringVar()
ntrpais = Entry(root,textvariable=pais)
ntrpais.grid(row=4, column=5, padx=5, pady=5)




Boton1 = Button(root, text='Enviar', command=lambda:guardar_datos(nombre.get(),apellido.get(),edad.get(),dni.get(),telefono.get(),email.get(),calle.get(),altura.get(),ciudad.get(),provincia.get(),pais.get()))
Boton1.grid(row = 20,column = 4, sticky="e",padx=5,pady=5 )

Boton1 = Button(root, text='Cancelar',command=lambda:root.quit())
Boton1.grid(row = 20,column = 5, sticky="e",padx=5,pady=5 )




root.mainloop()
