import tkinter as tk 
from tkinter import messagebox 
 
def nuevoDoctor(): 
    ventanaRegistro = tk.Toplevel(ventanaprincipal) 
    ventanaRegistro.title("Registro de Doctor") 
    ventanaRegistro.geometry("600x600") 
    ventanaRegistro.configure(bg="steelBlue") 
  
    # Nombre 
    nombreLabel = tk.Label(ventanaRegistro, text="Nombre: ", 
bg="lightBlue") 
    nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w") 
    entryNombre = tk.Entry(ventanaRegistro) 
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we") 
  
    # Dirección 
    direccionLabel = tk.Label(ventanaRegistro, text="Dirección: ", 
bg="lightBlue") 
    direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w") 
    entryDireccion = tk.Entry(ventanaRegistro) 
    entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we") 
  
    # Teléfono 
    telefonoLabel = tk.Label(ventanaRegistro, text="Teléfono: ", 
bg="lightBlue") 
    telefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w") 
    entryTelefono = tk.Entry(ventanaRegistro) 
    entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we") 
  
    # Horario (RadioButton) 
    horarioLabel = tk.Label(ventanaRegistro, text="Horario: ", 
bg="lightBlue") 
    horarioLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w") 
    horario = tk.StringVar(value="Mañana") 
    rbMañana = tk.Radiobutton(ventanaRegistro, text="Mañana", 
variable=horario, value="Mañana", bg="lightBlue") 
    rbMañana.grid(row=3, column=1, sticky="w") 
    rbTarde = tk.Radiobutton(ventanaRegistro, text="Tarde", 
variable=horario, value="Tarde", bg="lightBlue") 
    rbTarde.grid(row=4, column=1, sticky="w") 
    rbNoche = tk.Radiobutton(ventanaRegistro, text="Noche", 
variable=horario, value="Noche", bg="lightBlue") 
    rbNoche.grid(row=4, column=3, sticky="w") 
  
    enflabel=tk.Label(ventanaRegistro, text="especialidades: ", 
bg="lightblue") 
    enflabel.grid(row=5, column=0, padx=10, pady=5, sticky="w") 
    traumatologia=tk.BooleanVar() 
    cardiologia=tk.BooleanVar() 
    neurologia=tk.BooleanVar() 
    cbtraumatologia= tk.Checkbutton(ventanaRegistro,text="traumatologia", variable=traumatologia, bg="lightblue") 
    cbtraumatologia.grid(row=8, column=1, sticky="w") 
    cbcardiologia= tk.Checkbutton(ventanaRegistro,text="cardiologia", variable=cardiologia, bg="lightblue") 
    cbcardiologia.grid(row=9,column=1,sticky="w") 
    cbneurologia=tk.Checkbutton(ventanaRegistro,text="neurologia",variable=neurologia,bg="lightblue") 
    cbneurologia.grid(row=11,column=1,sticky="w") 
    #ACCION:REGISTRAR DATOS 
    def registrarDatos(): 
        especialidades=[] 
        if traumatologia.get(): 
            especialidades.append("traumatologia") 
        if cardiologia.get(): 
            especialidades.append("cardiologia") 
        if neurologia.get(): 
            especialidades.append()("neurologia") 
        if len(especialidades)>0: 
            especialidadesTexto=','.join(especialidades) 
        else: 
            especialidadesTexto='Ninguna' 
        info = ( 
            f"Nombre: {entryNombre.get()}\n" 
            f"Dirección: {entryDireccion.get()}\n" 
            f"Teléfono: {entryTelefono.get()}\n" 
            f"Horario: {horario.get()}\n" 
            f"especialidades:{especialidadesTexto}" 
        ) 
        messagebox.showinfo("Datos Registrados", info) 
        ventanaRegistro.destroy()  # cierra la ventana tras mostrar la info 
  
    # Botón para registrar 
    botonRegistrar = tk.Button(ventanaRegistro, text="Registrar", command=registrarDatos, bg="lightblue") 
    botonRegistrar.grid(row=13, column=0, columnspan=2, pady=10) 
  
def buscarDoctor(): 
    messagebox.showinfo("Buscar Doctor", "Función para buscar doctor") 
  
def eliminarDoctor(): 
    messagebox.showinfo("Eliminar Doctor", "Función para eliminar doctor") 
    
ventanaprincipal = tk.Tk() 
ventanaprincipal.title("Sistema de registro de pacientes")
ventanaprincipal.geometry("400x500") 
ventanaprincipal.configure(bg="skyblue") 
# barra de menú 
barraMenu = tk.Menu(ventanaprincipal) 
ventanaprincipal.config(menu=barraMenu) 
# menú de doctores 
menudoctores = tk.Menu(barraMenu, tearoff=0) 
barraMenu.add_cascade(label="Doctores", menu=menudoctores) 
menudoctores.add_command(label="Nuevo Doctor", command=nuevoDoctor) 
menudoctores.add_command(label="Buscar Doctor", command=buscarDoctor) 
menudoctores.add_command(label="Eliminar Doctor", command=eliminarDoctor) 
# menú de ayuda  
menuayuda = tk.Menu(barraMenu, tearoff=0) 
barraMenu.add_cascade(label="Ayuda", menu=menuayuda) 
menuayuda.add_command(label="Acerca de", command=lambda: 
messagebox.showinfo("Acerca de", "Comunicarse al 7784985")) 
ventanaprincipal.mainloop()