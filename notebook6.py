import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.font as font
from datetime import datetime

"""PACIENTES FUNCIONES"""
#FUNCION PARA ENMASCARAR FECHA
def enmascarar_fecha(texto):
    limpio="".join(filter(str.isdigit, texto))
    formato_final=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
    if FechaEntryP.get()!=formato_final:
        FechaEntryP.delete(0, tk.END)
        FechaEntryP.insert(0, formato_final)
    if len(FechaEntryP.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(FechaEntryP.get(), "%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True

#FUNCION PARA GUARDAR EL REGISTRO
def guardar_en_archivo():
    with open("paciente.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(f"""{paciente["Nombre"]}|{paciente["Fecha de Nacimiento"]}|{paciente["Edad"]}|{paciente["Género"]}|{paciente["Grupo Sanguíneo"]}|{paciente["Tipo de Seguro"]}|{paciente["Centro Médico"]}\n""")

#FUNCION PARA CARGAR DESDE EL ARCHIVO
def cargar_desde_archivo_pacientes():
    try:
        with open("paciente.txt", "r", encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==7:
                    paciente={
                        "Nombre":datos[0],
                        "Fecha de Nacimiento":datos[1],
                        "Edad":datos[2],
                        "Género":datos[3],
                        "Grupo Sanguíneo":datos[4],
                        "Tipo de Seguro":datos[5],
                        "Centro Médico":datos[6]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("paciente.txt", "w", encoding="utf-8").close()

#FUNCION PARA ELIMINAR REGISTRO DE PACIENTE
def eliminarPaciente():
    seleccionado=treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente", f"¿Estas seguro de eliminar el paciente '{treeview.item(id_item, 'values')[0]}'?"):
            del paciente_data[indice]
            guardar_en_archivo()
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente")
    else:
        messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningun paciente")
        return
        
#LISTA DE PACIENTES
paciente_data=[]

#FUNCION PARA REGISTRAR PACIENTES
def registrarPaciente():
    paciente={
        "Nombre":NombreEntryP.get(),
        "Fecha de Nacimiento":FechaEntryP.get(),
        "Edad":edadVar.get(), 
        "Género":genero.get(),
        "Grupo Sanguíneo":GrupoSanguineoEntry.get(),
        "Tipo de Seguro":tipoSeguro.get(),
        "Centro Médico":centroMedico.get()
    }
    #AGREGAR PACIENTE A LA LISTA
    paciente_data.append(paciente)
    #LLAMANDO A LA FUNCION PARA GUARDAR EN ARCHIVO
    guardar_en_archivo()
    #CARGAR EL TREEVIEW
    cargar_treeview()
    
#FUNCION PARA CARGAR TREEVIEW
def cargar_treeview():
    #LIMPIAR EL TREEVIEW
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #INSERTAR PACIENTE
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Género"],
                item["Grupo Sanguíneo"],
                item["Tipo de Seguro"],
                item["Centro Médico"]
            )
        )

"""DOCTORES FUNCIONES"""
#FUNCION PARA GUARDAR EL REGISTRO
def guardar_en_archivoD():
    with open("doctores.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(f"""{doctor["Nombre"]}|{doctor["Especialidad"]}|{doctor["Edad"]}|{doctor["Teléfono"]}\n""")
            
#FUNCION PARA CARGAR DESDE EL ARCHIVO
def cargar_desde_archivo_doctores():
    try:
        with open("doctores.txt", "r", encoding="utf-8") as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==4:
                    doctor={
                        "Nombre":datos[0],
                        "Especialidad":datos[1],
                        "Edad":datos[2],
                        "Teléfono":datos[3]
                    }
                    doctores_data.append(doctor)
        cargar_treeviewD()
    except FileNotFoundError:
        open("doctores.txt", "w", encoding="utf-8").close()

#FUNCION PARA ELIMINAR REGISTRO DE DOCTOR
def eliminarDoctor():
    seleccionado=treeview2.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente", f"¿Estas seguro de eliminar el paciente '{treeview2.item(id_item, 'values')[0]}'?"):
            del doctores_data[indice]
            guardar_en_archivoD()
            cargar_treeviewD()
            messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente")
    else:
        messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningun paciente")
        return
        
#FUNCION PARA CAMBIAR DE PESTAÑAS
def al_cambiar_pestañas(event):
    pestaña_activa=pestañas.index(pestañas.select())
    if pestaña_activa==0:
        cargar_desde_archivo_pacientes()
    elif pestaña_activa==1:
        cargar_desde_archivo_doctores()
        
#LISTA VACIA DE DOCTORES
doctores_data=[]

#REGISTRAR DOCTORES
def registrarDoctores():
    doctor={
        "Nombre":NombreEntryD.get(),
        "Especialidad":especialidad.get(),
        "Edad":spin.get(),
        "Teléfono":TelefonoEntryD.get()
    }
    #AGREGAR DOCTOR A LA LISTA
    doctores_data.append(doctor)
    #LLAMANDO A LA FUNCION PARA GUARDAR EN ARCHIVO
    guardar_en_archivoD()
    #CARGAR EL TREEVIEW
    cargar_treeviewD()

#FUNCION PARA CARGAR TREEVIEW EN DOCTORES
def cargar_treeviewD():
    #LIMPIAR EL TREEVIEW
    for doctor in treeview2.get_children():
        treeview2.delete(doctor)
    #INSERTAR DOCTOR
    for i, item in enumerate(doctores_data):
        treeview2.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Edad"],
                item["Teléfono"]
            )
        )

#CREACION DE LA VENTANA PRINCIPAL
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("800x600")

#SE CREA EL NOTEBOOK
pestañas=ttk.Notebook(ventanaPrincipal)

#SE CREAN LAS PESTAÑAS
framePacientes=ttk.Frame(pestañas)
frameDoctores=tk.Frame(pestañas, bg="silver")

#SE AGREGAN PESTAÑAS AL NOTEBOOK
pestañas.add(framePacientes, text="Pacientes")
pestañas.add(frameDoctores, text="Doctores")

#MOSTRAR LAS PESTAÑAS EN LA VENTANA
pestañas.pack(expand=True, fill="both")

"""PACIENTES"""
#NOMBRE
labelNombreP=tk.Label(framePacientes, text="Nombre Completo:")
labelNombreP.grid(row=0, column=0, sticky="w", pady=5, padx=5)
NombreEntryP=tk.Entry(framePacientes)
NombreEntryP.grid(row=0, column=1, sticky="w", pady=5, padx=5)

#FECHA DE NACIMIENTO
labelFechaP=tk.Label(framePacientes, text="Fecha de Nacimiento:")
labelFechaP.grid(row=1, column=0, sticky="w", pady=5, padx=5)
validacion_fecha=ventanaPrincipal.register(enmascarar_fecha)
FechaEntryP=ttk.Entry(framePacientes, validate="key", validatecommand=(validacion_fecha, "%P"))
FechaEntryP.grid(row=1, column=1, sticky="w", pady=5, padx=5)

#EDAD
labelEdadP=tk.Label(framePacientes, text="Edad:")
labelEdadP.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadVar=tk.StringVar()
EdadEntryP=tk.Entry(framePacientes, textvariable=edadVar, state="readonly")
EdadEntryP.grid(row=2, column=1, sticky="w", pady=5, padx=5)

#GENERO
labelGenero=tk.Label(framePacientes, text="Género:")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino")
radioMasculino=ttk.Radiobutton(framePacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(framePacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=3, column=2, sticky="w", padx=5)

#GRUPO SANGUINEO
labelGrupoSanguineo=tk.Label(framePacientes, text="Grupo Sanguíneo:")
labelGrupoSanguineo.grid(row=4, column=0, sticky="w", padx=5, pady=5)
GrupoSanguineoEntry=tk.Entry(framePacientes)
GrupoSanguineoEntry.grid(row=4, column=1, sticky="w", pady=5, padx=5)

#TIPO DE SEGURO
labelTipoSeguro=tk.Label(framePacientes, text="Tipo de Seguro:")
labelTipoSeguro.grid(row=5, column=0, sticky="w", padx=5, pady=5)
tipoSeguro=tk.StringVar()
tipoSeguro.set("Público")
comboTipoSeguro=ttk.Combobox(framePacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipoSeguro, state="readonly")
comboTipoSeguro.grid(row=5, column=1, sticky="w", pady=5, padx=5)

#CENTRO MEDICO
labelCentroMedico=tk.Label(framePacientes, text="Centro de Salud:")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centroMedico=tk.StringVar()
centroMedico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(framePacientes, values=["Hospital Central", "Clínica Norte", "Centro Sur"], textvariable=centroMedico, state="readonly")
comboCentroMedico.grid(row=6, column=1, sticky="w", pady=5, padx=5)

#FRAME PARA LOS BOTONES
btn_frame=tk.Frame(framePacientes)
btn_frame.grid(row=8, column=1, columnspan=2, pady=5, sticky="w")

#BOTON PARA REGISTRAR
btn_registrar=tk.Button(btn_frame, text="Registrar", command=lambda:registrarPaciente(), bg="green")
btn_registrar.grid(row=0, column=0, padx=5)

#BOTON ELIMINAR
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command=lambda:eliminarPaciente(), bg="red")
btn_eliminar.grid(row=0, column=1, padx=5)

#CREAR TREEVIEW PARA MOSTRAR PACIENTES
treeview=ttk.Treeview(framePacientes, columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM"), show="headings")

#DEFINIR ENCABEZADOS
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fexha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Médico")

#DEFINIR ANCHOS DE COLUMNAS
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)

#UBICAR EL TREEVIEW EN LA CUADRICULA
treeview.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)

#SCROLLBAR VERTICAL
scroll_y=ttk.Scrollbar(framePacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7, column=2, sticky="ns")



"""DOCTORES"""
#TITULO
tituloFont = font.Font(family="Arial", size=16, weight="bold")
labelTitulo=tk.Label(frameDoctores, text="REGISTRO DE DOCTORES", font=tituloFont, bg="silver")
labelTitulo.grid(row=0, column=1, sticky="w")

#NOMBRE
labelNombreD=tk.Label(frameDoctores, text="Nombre Completo:", bg="silver")
labelNombreD.grid(row=1, column=0, sticky="w", pady=5, padx=5)
NombreEntryD=tk.Entry(frameDoctores)
NombreEntryD.grid(row=1, column=1, sticky="w", pady=5, padx=5)

#ESPECIALIDAD
labelEspecialidad=tk.Label(frameDoctores, text="Especialidad:", bg="silver")
labelEspecialidad.grid(row=2, column=0, sticky="w", padx=5, pady=5)
especialidad=tk.StringVar()
especialidad.set("Cardiología")
comboEspecialidad=ttk.Combobox(frameDoctores, values=["Cardiología", "Neurología", "Pediatría", "Traumatología"], textvariable=especialidad, state="readonly")
comboEspecialidad.grid(row=2, column=1, sticky="w", pady=5, padx=5)

#EDAD
labelEdad=tk.Label(frameDoctores, text="Edad:", bg="silver")
labelEdad.grid(row=3, column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(frameDoctores, from_=18, to=100, state="readonly")
spin.grid(row=3, column=1, padx=10, pady=10, sticky="w")

#TELEFONO
labelTelefono=tk.Label(frameDoctores, text="Teléfono:", bg="silver")
labelTelefono.grid(row=4, column=0, sticky="w", padx=5, pady=5)
TelefonoEntryD=tk.Entry(frameDoctores)
TelefonoEntryD.grid(row=4, column=1, sticky="w", pady=5, padx=5)

#FRAME PARA LOS BOTONES
btn_frame2=tk.Frame(frameDoctores)
btn_frame2.grid(row=6, column=1, columnspan=2, pady=5, sticky="w")

#BOTON PARA REGISTRAR
btn_registrar2=tk.Button(btn_frame2, text="Registrar", command=lambda:registrarDoctores(), bg="green")
btn_registrar2.grid(row=0, column=0, padx=5)

#BOTON ELIMINAR
btn_eliminar2=tk.Button(btn_frame2, text="Eliminar", command="", bg="red")
btn_eliminar2.grid(row=0, column=1, padx=5)

#CREAR TREEVIEW PARA MOSTRAR DOCTORES
treeview2=ttk.Treeview(frameDoctores, columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")

#DEFINIR ENCABEZADOS
treeview2.heading("Nombre", text="Nombre Completo")
treeview2.heading("Especialidad", text="Especialidad")
treeview2.heading("Edad", text="Edad")
treeview2.heading("Telefono", text="Teléfono")

#DEFINIR ANCHOS DE COLUMNAS
treeview2.column("Nombre", width=120)
treeview2.column("Especialidad", width=120)
treeview2.column("Edad", width=50, anchor="center")
treeview2.column("Telefono", width=60, anchor="center")

#UBICAR EL TREEVIEW EN LA CUADRICULA
treeview2.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)

#SCROLLBAR VERTICAL
scroll_y2=ttk.Scrollbar(frameDoctores, orient="vertical", command=treeview2.yview)
treeview2.configure(yscrollcommand=scroll_y2.set)
scroll_y2.grid(row=5, column=2, sticky="ns")

#ASOCIAR EVENTO DE CAMBIO DE PESTAÑAS
pestañas.bind("<<NotebookTabChanged>>", al_cambiar_pestañas)

#CARGAR DATOS DESDE EL ARCHIVO AL INICIAR LA APLICACION
cargar_desde_archivo_pacientes()

ventanaPrincipal.mainloop()
