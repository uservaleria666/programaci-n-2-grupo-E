import tkinter as tk
from tkinter import ttk, messagebox
 
# Lista de doctores
lista_doctores = []
 
# Guardar doctores en archivo
def guardar_doctores():
    with open("doctores.txt", "w", encoding="utf-8") as archivo:
        for doctor in lista_doctores:
            archivo.write(f"{doctor['nombre']}|{doctor['especialidad']}|{doctor['años experiencia']}|{doctor['telefono']}|{doctor['hospital']}|{doctor['genero']}\n")
 
# Cargar doctores desde archivo
def cargar_doctores():
    try:
        with open("doctores.txt", "r", encoding="utf-8") as archivo:
            lista_doctores.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 6:
                    doctor = {
                        "nombre": datos[0],
                        "especialidad": datos[1],
                        "años experiencia": datos[2],
                        "telefono": datos[3],
                        "hospital": datos[4],
                        "genero": datos[5]
                    }
                    lista_doctores.append(doctor)
        actualizar_tabla()
    except FileNotFoundError:
        open("doctores.txt", "w", encoding="utf-8").close()
 
# Registrar nuevo doctor
def registrar_doctor():
    doctor = {
        "nombre": entrada_nombre.get(),
        "especialidad": seleccion_especialidad.get(),
        "años experiencia": entrada_edad.get(),
        "telefono": entrada_telefono.get(),
        "hospital": seleccion_hospital.get(),
        "genero": seleccion_genero.get()
    }
    lista_doctores.append(doctor)
    guardar_doctores()
    actualizar_tabla()
 
# Actualizar tabla
def actualizar_tabla():
    for item in tabla_doctores.get_children():
        tabla_doctores.delete(item)
    for i, doctor in enumerate(lista_doctores):
        tabla_doctores.insert("", "end", iid=str(i), values=(
            doctor["nombre"],
            doctor["especialidad"],
            doctor["años experiencia"],
            doctor["telefono"],
            doctor["hospital"],
            doctor["genero"]
        ))
 
# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Doctores")
ventana.geometry("750x600")
 
# Formulario
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)
 
tk.Label(ventana, text="Especialidad:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
seleccion_especialidad = tk.StringVar()
ttk.Combobox(ventana, textvariable=seleccion_especialidad, values=["Cardiología", "Pediatría", "Neurología", "Traumatología"]).grid(row=1, column=1, padx=5, pady=5)
 
tk.Label(ventana, text="Años Experiencia:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entrada_edad = tk.Spinbox(ventana, from_=0, to=100)
entrada_edad.grid(row=2, column=1, padx=5, pady=5)
entrada_edad.delete(0, tk.END)
entrada_edad.insert(0, "1")
 
tk.Label(ventana, text="Teléfono:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entrada_telefono = tk.Entry(ventana)
entrada_telefono.grid(row=3, column=1, padx=5, pady=5)
 
tk.Label(ventana, text="Hospital:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
seleccion_hospital = tk.StringVar()
ttk.Combobox(ventana, textvariable=seleccion_hospital, values=[
    "Hospital Central",
    "Hospital Norte",
    "Clínica Santa María",
    "Clínica Vida"
]).grid(row=4, column=1, padx=5, pady=5)
 
tk.Label(ventana, text="Género:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
seleccion_genero = tk.StringVar()
seleccion_genero.set("Masculino")
tk.Radiobutton(ventana, text="Masculino", variable=seleccion_genero, value="Masculino").grid(row=5, column=1, sticky="w")
tk.Radiobutton(ventana, text="Femenino", variable=seleccion_genero, value="Femenino").grid(row=5, column=1, padx=100, sticky="w")
 
# Botones
marco_botones = tk.Frame(ventana)
marco_botones.grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(marco_botones, text="Registrar", bg="green", fg="white", command=registrar_doctor).grid(row=0, column=0, padx=5)
 
# Tabla
tabla_doctores = ttk.Treeview(ventana, columns=("Nombre", "Especialidad", "Años Experiencia", "Teléfono", "Hospital", "Género"), show="headings")
for columna in ("Nombre", "Especialidad", "Años Experiencia", "Teléfono", "Hospital", "Género"):
    tabla_doctores.heading(columna, text=columna)
    tabla_doctores.column(columna, width=110)
tabla_doctores.grid(row=7, column=0, columnspan=2, padx=5, pady=10)
 
scroll = ttk.Scrollbar(ventana, orient="vertical", command=tabla_doctores.yview)
tabla_doctores.configure(yscrollcommand=scroll.set)
scroll.grid(row=7, column=2, sticky="ns")
 
# Cargar datos al iniciar
cargar_doctores()
 
# Ejecutar app
ventana.mainloop()
 
 