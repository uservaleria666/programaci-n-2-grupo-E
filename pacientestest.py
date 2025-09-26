#Importar librerias
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
 
#Funciones para Pacientes
#funcion para enmascarar fecha
def enmascarar_fecha(texto):
    limpio = "".join(filter(str.isdigit, texto))
    formato_final = ""
    if len(limpio) > 8:
        limpio = limpio[:8]
    if len(limpio) > 4:
        formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio) > 2:
        formato_final = f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final = limpio
   
    if fechaP.get() != formato_final:
        fechaP.delete(0, tk.END)
        fechaP.insert(0, formato_final)    
       
    if len(fechaP.get()) == 10:
        fecha_actual = datetime.now().date()
        fecha_nacimiento = datetime.strptime(fechaP.get(), "%d-%m-%Y").date()
        edad = fecha_actual.year - fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
 
#Guardar pacientes en archivo
def guardar_en_archivo():
    with open("pacientePeso.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"
                          f"{paciente['Genero']}|{paciente['Grupo Sanguineo']}|"
                          f"{paciente['Tipo de Seguro']}|{paciente['Centro Medico']}|{paciente['Peso']}\n")          
 
#Cargar desde archivo pacientes
def cargar_desde_archivo_pacientes():
    try:
        with open("pacientePeso.txt", "r", encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 8:
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Genero": datos[3],
                        "Grupo Sanguineo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Medico": datos[6],
                        "Peso": datos[7]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("pacientePeso.txt", "w", encoding="utf-8").close()
 
#funcion eliminar paciente
def eliminar_paciente():
    seleccionado = treeview.selection()
    if seleccionado:
        indice = int(seleccionado[0])      
        id_item = seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente", f"¿Estas seguro de eliminar al paciente {treeview.item(id_item, 'values')[0]}?"):
            del paciente_data[indice]
            guardar_en_archivo() #Guarda los cambios en el archivo
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente")
    else:
        messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningun paciente.")
 
#lista de pacientes (inicialmente vacia)
paciente_data = []
 
#funcion para registrar pacientes
def registrarPaciente():
    paciente = {
        "Nombre": nombreP.get(),
        "Fecha de Nacimiento": fechaP.get(),
        "Edad": edadVar.get(),
        "Genero": genero.get(),
        "Grupo Sanguineo": entryGrupoSanguineo.get(),
        "Tipo de Seguro": tipo_seguro.get(),
        "Centro Medico": centro_medico.get(),
        "Peso": entryPeso.get()
    }
    paciente_data.append(paciente)
    guardar_en_archivo()
    cargar_treeview()
 
def cargar_treeview():
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Grupo Sanguineo"],
                item["Tipo de Seguro"],
                item["Centro Medico"],
                item["Peso"]
            )
        )

# ventana Principal
ventana_principal = tk.Tk()
ventana_principal.title("Libro de pacientes")
ventana_principal.geometry("900x900")
 
#Crear contenedor Notebook(pestañas)
pestañas = ttk.Notebook(ventana_principal)
 
#crear frames (uno por pestaña)
frame_pacientes = ttk.Frame(pestañas)
frame_doctores = ttk.Frame(pestañas)
 
#Agregar pestañas al notebook
pestañas.add(frame_pacientes, text="Pacientes")
pestañas.pack(expand=True, fill="both")
 
# Formulario pacientes
labelNombre = tk.Label(frame_pacientes, text= "Nombre Completo:")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP = tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)
 #Fecha de nacimiento
labelNacimiento = tk.Label(frame_pacientes, text= "Fecha de Nacimiento:")
labelNacimiento.grid(row=1, column=0, sticky="w", pady=5, padx=5)
validacion_fecha = ventana_principal.register(enmascarar_fecha)
fechaP = ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha, "%P"))
fechaP.grid(row=1, column=1, sticky="w", pady=5, padx=5)
 #Edad
labelEdad = tk.Label(frame_pacientes, text="Edad:")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadVar = tk.StringVar()
edadP = tk.Entry(frame_pacientes, textvariable=edadVar, state="readonly")
edadP.grid(row=2, column=1, sticky="w", pady=5, padx=5)
#Genero
labelGenero = tk.Label(frame_pacientes, text="Genero:")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero = tk.StringVar()
genero.set("Masculino")
radioMasculino = ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino = ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)
#Grupo Sanguineo
labelGrupoSanguineo = tk.Label(frame_pacientes, text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", padx=5, pady=5)
entryGrupoSanguineo = tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5, column=1, sticky="w", padx=5, pady=5)
#Tipo de Seguro
labelTipoSeguro = tk.Label(frame_pacientes, text="Tipo de seguro:")
labelTipoSeguro.grid(row=6, column=0, sticky="w", pady=5, padx=5)
tipo_seguro = tk.StringVar()
tipo_seguro.set("Publico")
comboTipoSeguro = ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6, column=1, sticky="w", pady=5, padx=5)
#Centro de Salud
labelCentroMedico = tk.Label(frame_pacientes, text="Centro de salud:")
labelCentroMedico.grid(row=7, column=0, sticky="w", padx=5, pady=5)
centro_medico = tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico = ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5)
#Peso
labelPeso = tk.Label(frame_pacientes, text="Peso:")
labelPeso.grid(row=8, column=0, sticky="w", padx=5, pady=5)
entryPeso = tk.Entry(frame_pacientes)
entryPeso.grid(row=8, column=1, sticky="w", padx=5, pady=5)
 
btn_frame = tk.Frame(frame_pacientes)
btn_frame.grid(row=9, column=0, columnspan=2, pady=5, sticky="w")
 
btn_registrar = tk.Button(btn_frame, text="Registrar", command=registrarPaciente)
btn_registrar.grid(row=0, column=0, padx=5)
btn_eliminar = tk.Button(btn_frame, text="Eliminar", command=eliminar_paciente)
btn_eliminar.grid(row=0, column=1, padx=5)
 
treeview = ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM", "Peso"), show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Medico")
treeview.heading("Peso", text="Peso")
treeview.column("Nombre", width=120)

treeview.column("Edad", width=120, anchor="center")
treeview.column("Genero", width=50, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120, anchor="center")
treeview.column("Peso", width=100, anchor="center")
treeview.grid(row=10, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
scroll_y = ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7, column=2, sticky="ns")
  
cargar_desde_archivo_pacientes()
ventana_principal.mainloop()
 
 