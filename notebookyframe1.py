#importacion de librerias
import tkinter as tk 
from tkinter import ttk,messagebox
 
#crear ventana principal
ventana_principal= tk.Tk()
ventana_principal.title("Libro de pacientes y doctores")
ventana_principal.geometry("400x600") 

#Crear contenedor Notebook(pesttañas)
pestañas=ttk.Notebook(ventana_principal)

#crear frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)

#Agregar pestañas al notebook
pestañas.add(frame_pacientes,text="Pacientes")

#Mostrar las pestañas en la ventaña
pestañas.pack(expand=True, fill="both")

#Crear pestaña doctores
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores,text="Doctores")
pestañas.pack(expand=True, fill="both")

#Nombre
labelNombre=tk.Label(frame_pacientes, text= "Nombre Completo:")
labelNombre.grid(row=0,column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1, sticky="w", pady=5, padx=5)

#Fecha de nacimiento 
labelNacimiento=tk.Label(frame_pacientes, text= "Fecha de Nacimiento:")
labelNacimiento.grid(row=1,column=0, sticky="w", pady=5, padx=5)
fechaP=tk.Entry(frame_pacientes)
fechaP.grid(row=1,column=1, sticky="w", pady=5, padx=5)

#Edad (readonly)
labelEdad=tk.Label(frame_pacientes, text="Edad:")
labelEdad.grid(row=2,column=0, sticky="w", pady=5,padx=5)
edadP=tk.Entry(frame_pacientes,state="readonly")
edadP.grid(row=2, column=1, sticky="w",pady=5, padx=5)

#Genero
labelGenero=tk.Label(frame_pacientes, text="Genero:")
labelGenero.grid(row=3, column=0,sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino") #Valor por Defecto
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino",variable=genero, value="Femenino")
radioFemenino.grid(row=4,column=1, sticky="w",padx=5)

#Grupo sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", padx=5, pady=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5, column=1,sticky="w",padx=5,pady=5)

#Tipos de seguro
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de seguro:")
labelTipoSeguro.grid(row=6, column=0, sticky="w", pady=5, padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")# valor por defaut
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Publico","Privado","Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6,column=1,sticky="w",pady=5,padx=5)

#CENTRO MEDICO
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de salud:")
labelCentroMedico.grid(row=7, column=0,sticky="w",padx=5, pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")#Valor por deafut
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central","Clinica Norte","Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w",padx=5,pady=5)





ventana_principal.mainloop()
