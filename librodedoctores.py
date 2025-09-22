import tkinter as tk
from tkinter import ttk, messagebox
 
# Lista de doctores
doctores_data = []
 
# Guardar doctores en archivo
def guardar_doctores():
    with open("doctoresRegistro.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['Edad']}|{doctor['Telefono']}|{doctor['Genero']}|{doctor['Hospital']}\n")
 
# Cargar doctores desde archivo
def cargar_desde_archivo():
    try:
        with open("doctoresRegistro.txt", "r", encoding="utf-8") as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 6:
                    doctor = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Edad": datos[2],
                        "Telefono": datos[3],
                        "Genero": datos[4],
                        "Hospital": datos[5]
                    }
                    doctores_data.append(doctor)
        cargar_treeview()
    except FileNotFoundError:
        open("doctoresRegistro.txt", "w", encoding="utf-8").close()
 
# Registrar nuevo doctor
def registrar_doctor():
    doctor = {
        "Nombre": entry_nombre.get(),
        "Especialidad": especialidad_var.get(),
        "Edad": spin_edad.get(),
        "Telefono": entry_telefono.get(),
        "Genero": genero_var.get(),
        "Hospital": hospital_var.get()
    }
    doctores_data.append(doctor)
    guardar_doctores()
    cargar_treeview()
    limpiar_formulario()
 
# Cargar datos en tabla
def cargar_treeview():
    for item in treeview.get_children():
        treeview.delete(item)
    for i, doctor in enumerate(doctores_data):
        treeview.insert("", "end", iid=str(i), values=(
            doctor["Nombre"],
            doctor["Especialidad"],
            doctor["Edad"],
            doctor["Telefono"],
            doctor["Hospital"],
        ))
 
# Limpiar formulario
def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    especialidad_var.set("")
    spin_edad.delete(0, tk.END)
    spin_edad.insert(0, "25")
    entry_telefono.delete(0, tk.END)
    genero_var.set("")
    hospital_var.set("")
 
# Ventana principal
ventana = tk.Tk()
ventana.title("Libro de Doctores")
ventana.geometry("1000x800")
 
# Pestañas
pestañas = ttk.Notebook(ventana)
pestañas.pack(fill="both", expand=True)
 
# Pestaña Doctores
frame_doctores = ttk.Frame(pestañas)
pestañas.add(frame_doctores, text="Doctores")
 
# Título
tk.Label(frame_doctores, text="Registro de Doctores", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)
 
# Formulario
tk.Label(frame_doctores, text="Nombre:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_nombre = tk.Entry(frame_doctores)
entry_nombre.grid(row=1, column=1, columnspan=2, sticky="w", padx=5)
 
tk.Label(frame_doctores, text="Especialidad:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
especialidad_var = tk.StringVar()
ttk.Combobox(frame_doctores, textvariable=especialidad_var, values=["Cardiología", "Pediatría", "Neurología", "Traumatologia"]).grid(row=2, column=1, columnspan=2, sticky="w", padx=5)
 
tk.Label(frame_doctores, text="Años Experiencia:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
spin_edad = tk.Spinbox(frame_doctores, from_=0, to=60)
spin_edad.grid(row=3, column=1, columnspan=2, sticky="w", padx=5)
spin_edad.delete(0, tk.END)
spin_edad.insert(0, "1")
 
tk.Label(frame_doctores, text="Género:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
genero_var = tk.StringVar()
tk.Radiobutton(frame_doctores, text="Masculino", variable=genero_var, value="Masculino").grid(row=4, column=1, sticky="w")
tk.Radiobutton(frame_doctores, text="Femenino", variable=genero_var, value="Femenino").grid(row=4, column=2, sticky="w")
 
tk.Label(frame_doctores, text="Hospital:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
hospital_var = tk.StringVar()
ttk.Combobox(frame_doctores, textvariable=hospital_var, values=["Hospital Central", "Clínica Vida", "San Juan", "Otro"]).grid(row=5, column=1, columnspan=2, sticky="w", padx=5)
 
tk.Label(frame_doctores, text="Teléfono:").grid(row=6, column=0, sticky="e", padx=5, pady=5)
entry_telefono = tk.Entry(frame_doctores)
entry_telefono.grid(row=6, column=1, columnspan=2, sticky="w", padx=5)
 
# Botón Registrar
tk.Button(frame_doctores, text="Registrar", bg="green", fg="white", command=registrar_doctor).grid(row=7, column=1, pady=10)

# Tabla
treeview = ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Telefono","Hospital"), show="headings")
treeview.heading("Nombre", text="Nombre")
treeview.heading("Especialidad", text="Especialidad")
treeview.heading("Edad", text="Edad")
treeview.heading("Telefono", text="Teléfono")
treeview.heading("Hospital", text="Hospital")
treeview.grid(row=8, column=0, columnspan=3, padx=5, pady=10, sticky="nsew")
 
scroll = ttk.Scrollbar(frame_doctores, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll.set)
scroll.grid(row=8, column=3, sticky="ns")
 
# Cargar datos al iniciar
cargar_desde_archivo()
 
# Ejecutar app
ventana.mainloop()