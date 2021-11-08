from tkinter import *
from form import *
from formmedic import alta_de_medico
from turnos import *

root = Tk()
root.title("Sanatorio paso al infierno")
root.geometry("600x400")





# entrada = Entry(root, width=20)
# entrada.grid(row=0)

CrearUsuario = Button(root,text="Alta de paciente",command=lambda:alta_de_paciente()).grid(row=1,column=7)
BuscarUsuario = Button(root,text="Buscar").grid(row=2,column=7)
CrearUsuario = Button(root,text="Alta de medico",command=lambda:alta_de_medico()).grid(row=3,column=7)
SacarTurno = Button(root, text="Sacar Turno",command=lambda:turnos()).grid(row=4)



mainloop()
