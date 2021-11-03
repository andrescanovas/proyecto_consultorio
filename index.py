from tkinter import *
from form import *

root = Tk()
root.title("Sanatorio paso al infierno")
root.geometry("600x400")





# entrada = Entry(root, width=20)
# entrada.grid(row=0)

CrearUsuario = Button(root,text="Alta",command=lambda:alta_de_paciente()).grid(row=1)
BuscarUsuario = Button(root,text="Buscar").grid(row=1,column=2)

mainloop()
