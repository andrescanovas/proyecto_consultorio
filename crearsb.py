import sqlite3
from tkinter import messagebox


def guardar_datos(nombre,apellido,edad,dni,telefono,email,calle,altura,ciudad,provincia,pais,medicoCabe):
    
    """En esta funcion se crea la base de datos si no exite y se agregan los datos """

    conexion = sqlite3.connect("bd.db")
    micursor = conexion.cursor()
    try:
        micursor.execute("""
                            create table pacientes(
                            id integer primary key autoincrement,
                            nombre text,
                            apellido text,
                            edad numeric,
                            dni numeric,
                            telefono numeric,
                            email text,
                            calle text,
                            altura text,
                            ciudad text,
                            provincia text,
                            pais text,
                            medicoCabe text
                            )
                        """)
        print("Se ha creado exitosamente la tabla pacientes")
    except sqlite3.OperationalError:
        print("la tabla articula ya existe")
    conexion.close()

    conexion=sqlite3.connect("bd.db")
    micursor = conexion.cursor()
    

    datos=nombre.get(),apellido.get(),edad.get(),dni.get(),telefono.get(),email.get(),calle.get(),altura.get(),ciudad.get(),provincia.get(),pais.get(),medicoCabe.get()
    micursor.execute("insert into pacientes values(NULL,?,?,?,?,?,?,?,?,?,?,?,?)",(datos))
    
    

    conexion.commit()
    conexion.close()

    

    




# nombre = input("ingrese su nombre: ")
# edad = int(input("ingrese su edad: "))


# print(guardar_datos(nombre,edad))



def guardar_datos_de_medicos(nombre,apellido,edad,dni,telefono,email,calle,altura,ciudad,provincia,pais,medicoCabe):
    
    """En esta funcion se crea la base de datos y la tabla medicos si no exite y se agregan los datos """

    conexion = sqlite3.connect("bd.db")
    micursor = conexion.cursor()
    try:
        micursor.execute("""
                            create table medicos(
                            id integer primary key autoincrement,
                            nombre text,
                            apellido text,
                            edad numeric,
                            dni numeric,
                            telefono numeric,
                            email text,
                            calle text,
                            altura text,
                            ciudad text,
                            provincia text,
                            pais text,
                            medicoCabe
                            )
                        """)
        print("Se ha creado exitosamente la tabla medicos")
    except sqlite3.OperationalError:
        print("la tabla articula ya existe")
    conexion.close()

    conexion=sqlite3.connect("bd.db")
    micursor = conexion.cursor()
    
    
    datos=nombre.get(),apellido.get(),edad.get(),dni.get(),telefono.get(),email.get(),calle.get(),altura.get(),ciudad.get(),provincia.get(),pais.get(),medicoCabe.get()
    micursor.execute("insert into medicos values(NULL,?,?,?,?,?,?,?,?,?,?,?,?)",(datos))
    

    conexion.commit()
    conexion.close()



def buscar_pacientes_all():
    """ Esta funcion se usa para traer todos los datos de los pacientes"""
    conexion = sqlite3.connect("bd.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM pacientes")

    pacientes = cursor.fetchall()

    for cliente in pacientes:
        print(cliente)

    conexion.commit()
    conexion.close()

# ============================BUSCAR PACIENTES===========================

    # def buscar_pacientes_por_nombre(nombre):
        # """ Esta funcion se usa para traer los datos de los pacientes individualmente por nombre """

# nombre = "Andres"

# conexion = sqlite3.connect("bd.db")
# cursor = conexion.cursor()
# sqlcon = "SELECT * FROM pacientes WHERE nombre = ?;"
# cursor.execute(sqlcon,(nombre,))

# registros = cursor.fetchall()

# for r in registros:
#     print(r)

# conexion.commit()
# conexion.close()

# print()


    


        


# print(buscar_pacientes


def editar_un_usuario(usuario):
    conexion = sqlite3.connect("bd.db")

    cursor = conexion.cursor()

    cursor.execute("UPDATE pacientes set nombre='nombre'"  "WHERE edad=edad")

    conexion.commit()
    conexion.close()


def limpiar_campos_pacientes(nombre,apellido,edad,dni,telefono,email,calle,altura,ciudad,provincia,pais):
    nombre.set("")
    apellido.set("")
    edad.set("")
    dni.set("")
    telefono.set("")
    email.set("")
    calle.set("")
    altura.set("")
    ciudad.set("")
    provincia.set("")
    pais.set("")


def cerrar_sistema(hola):
    if messagebox.askokcancel("Quit", "Quieres salir del Sistema de Turnos?"):
        hola.destroy()




