import tkinter as tk
from tkinter import ttk
#Crear ventana principal
ventana=tk.Tk()
ventana.title("Ejemplo combobox")
ventana.geometry("300x200")
#etiqueta
etiqueta=tk.Label(ventana,text="Seleccion especialidad:")
etiqueta.grid(row=0,column=0,padx=10,pady=10,sticky="w")
#crear combobox
opciones=["Cardiologia","Neurologia","Pediatria","Dermatologia"]
combo=ttk.Combobox(ventana,values=opciones,state="readonly")
combo.current(0) #Seleccionar primera opcion por defecto
combo.grid(row=0,column=1, padx=10,pady=10)
#Funcion para mostrar la seleccion
def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("seleccion",f"Has elegido:{seleccion}")
#Boton para confirmar seleccion
boton=tk.Button(ventana,text="Aceptar",command=mostrar)
boton.grid(row=1,column=0, columnspan=2,pady=15)
ventana.mainloop()