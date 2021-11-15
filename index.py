# Importar Bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from crearsb import *
from formPacientes import *
from formmedic import *
import sqlite3

from turnos import turnos


# Desarrollo de la Interfaz grafica
root=Tk()
root.title("Base de Datos de pacientes")
root.geometry("1024x640")


miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miEdad=StringVar()
miDNI =StringVar()
miTelefono=StringVar()
miEmail = StringVar()

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miApellido.set("")
	miEdad.set("")
	miDNI.set("")
	miTelefono.set("")
	miEmail.set("")
	
def mensaje():
	acerca='''
	Aplicación CRUD
	Version 1.0
	Tecnología Python Tkinter
	'''
	messagebox.showinfo(title="INFORMACION", message=acerca)


                ################################## Tabla ################################
				
tree=ttk.Treeview(height=20, columns=('#0','#1','#2','#3','#4','#5'))
tree.place(x=0, y=200)
tree.column('#0',width=50)
tree.heading('#0', text="ID", anchor=CENTER)
tree.heading('#1', text="Nombre", anchor=CENTER)
tree.heading('#2', text="Apellido", anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#3', text="Edad", anchor=CENTER)
tree.column('#4',width=100)
tree.heading('#4',text="DNI",anchor=CENTER)
tree.heading('#5',text="Telefono",anchor=CENTER)
tree.heading('#6',text="E-mail",anchor=CENTER)

def seleccionarUsandoClick(event):
	item=tree.identify('item',event.x,event.y)
	miId.set(tree.item(item,"text"))
	miNombre.set(tree.item(item,"values")[0])
	miApellido.set(tree.item(item,"values")[1])
	miEdad.set(tree.item(item,"values")[2])
	miDNI.set(tree.item(item,"values")[3])
	miTelefono.set(tree.item(item,"values")[4])
	miEmail.set(tree.item(item,"values")[5])


tree.bind("<Double-1>", seleccionarUsandoClick)


def mostrar(tipo):

	""" En esta funcion se muestran los registros de las tablas "paciente" y "medico" de la base de datos bd """
	miConexion=sqlite3.connect("bd.db")
	miCursor=miConexion.cursor()
	registros=tree.get_children()
	for elemento in registros:
		tree.delete(elemento)

	try:
		if tipo==0:
			tipo1="pacientes"
			
			ltipos.config(text='PACIENTES')
		else:
			tipo1="medicos"
			ltipos.config(text='MEDICOS')
		miCursor.execute("SELECT * FROM " + tipo1)
		for row in miCursor:
			tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
	except:
		pass

def actualizar():
	miConexion=sqlite3.connect("bd.db")
	miCursor=miConexion.cursor()
	try:
		
		if ltipos.cget("text") == "PACIENTES":
			tipo1="pacientes"
			tipo2=0
		else:
			tipo1="medicos"
			tipo2=1

		datos=miNombre.get(),miApellido.get(),miEdad.get(),miDNI.get(),miTelefono.get(),miEmail.get()
		miCursor.execute("UPDATE "+ tipo1 +" SET NOMBRE=?, Apellido=?, Edad=?, dni=?, telefono=?, email=? WHERE ID="+miId.get(), (datos))
		
		miConexion.commit()
	except:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
		pass
	limpiarCampos()
	mostrar(tipo2)
	


def borrar():
	miConexion=sqlite3.connect("bd.db")
	miCursor=miConexion.cursor()
	try:
		if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
			miCursor.execute("DELETE FROM pacientes WHERE ID="+miId.get())
			miConexion.commit()
	except:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
		pass
	limpiarCampos()
	mostrar()

###################### Colocar widgets en la VISTA ######################
########## Creando Los menus ###############
menubar=Menu(root)
menubasedat=Menu(menubar,tearoff=0)
# menubasedat.add_command(label="Crear/Conectar Base de Datos", command=conexionBBDD)
menubasedat.add_command(label="Agregar medico", command=lambda:alta_de_medico())
menubasedat.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda",menu=ayudamenu)

############## Creando etiquetas y cajas de texto ###########################
e1=Entry(root, textvariable=miId)

# l2=Label(root, text="Nombre")
# l2.place(x=20,y=10)
# e2=Entry(root, textvariable=miNombre)
# e2.place(x=80, y=10)

# l3=Label(root, text="Apellido")
# l3.place(x=250,y=10)
# e3=Entry(root, textvariable=miApellido)
# e3.place(x=320, y=10)

# l4=Label(root, text="Edad")
# l4.place(x=450,y=10)
# e4=Entry(root, textvariable=miEdad, width=10)
# e4.place(x=500, y=10)

# l5=Label(root, text="DNI")
# l5.place(x=600,y=10)
# e5=Entry(root, textvariable=miDNI, width=10)
# e5.place(x=640, y=10)



l2=Label(root, text="Nombre")
l2.grid(pady=10,row=1, column=0)
e2=Entry(root, textvariable=miNombre)
e2.grid(pady=10,row=1, column=1)

l3=Label(root, text="Apellido")
l3.grid(pady=10,row=1, column=2)
e3=Entry(root, textvariable=miApellido)
e3.grid(pady=10,row=1, column=3)

l4=Label(root, text="Edad")
l4.grid(pady=10,row=1, column=4)
e4=Entry(root, textvariable=miEdad, width=10)
e4.grid(pady=10,row=1, column=5)

l5=Label(root, text="DNI")
l5.grid(pady=10,row=1, column=6)
e5=Entry(root, textvariable=miDNI, width=10)
e5.grid(pady=10,row=1, column=7) 

l6=Label(root, text="Telefono")
l6.grid(row=2, column=0)
e6=Entry(root, textvariable=miTelefono)
e6.grid(row=2, column=1) 

l7=Label(root, text="E-mail")
l7.grid(row=2, column=2)
e7=Entry(root, textvariable=miEmail)
e7.grid(row=2, column=3) 



# =========================RECIEIENDO DATOS DEL TREEVIEW==============
def crear_turno():  
	""" Esta funcion sirve para imprimir los datos capturados del item del tree mediante curItem"""  
	miConexion=sqlite3.connect("bd.db")
	miCursor=miConexion.cursor()
	
	curItem = tree.focus()
	nombre = tree.item(curItem)["values"][0]
	apellido = tree.item(curItem)["values"][1]
	dni = tree.item(curItem)["values"][3]

	# print(tree.item(curItem))

	dato = miCursor.execute("SELECT * FROM pacientes WHERE dni like '%"+dni+"%'")
	
	print(tree.item(curItem)["values"][0],tree.item(curItem)["values"][1])
	# print(dato.fetchall())

	


################# Creando botones ###########################

b1=Button(root, text="Crear Registro", command=alta_de_paciente)
b1.place(x=20, y=90)
b2=Button(root, text="Modificar Registro", command=actualizar)
b2.place(x=145, y=90)
b3=Button(root, text="Mostrar paciente", command=lambda:mostrar(0))
b3.place(x=20, y=125)

b4=Button(root, text="Eliminar Registro",bg="red", command=borrar)
b4.place(x=300, y=90)
b5=Button(root, text="Mostrar medico", command=lambda:mostrar(1))
b5.place(x=160, y=125)
b6=Button(root,text="CREAR TURNO",command=crear_turno)
b6.place(x=550, y=125)



################ LABEL DONDE SE MUESTRA SI EN LA LISTA HAY PACIENTE O MEDICOS "LABEL TIPOS: este label muestra si es medicos y pacientes"############################33

ltipos=Label(root, text="",)
ltipos.place(x=300,y=170)


def mostrar(tipo):

	""" En esta funcion se muestran los registros de las tablas "paciente" y "medico" de la base de datos bd """
	miConexion=sqlite3.connect("bd.db")
	miCursor=miConexion.cursor()
	registros=tree.get_children()
	for elemento in registros:
		tree.delete(elemento)

	try:
		if tipo==0:
			tipo1="pacientes"
			
			ltipos.config(text='PACIENTES')
		else:
			tipo1="medicos"
			ltipos.config(text='MEDICOS')
		miCursor.execute("SELECT * FROM " + tipo1)
		for row in miCursor:
			tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
	except:
		pass





root.config(menu=menubar)


root.mainloop()