import tkinter as tk
from tkinter import ttk, messagebox

# Lista de medicamentos (estructura en memoria)
medicamentos_data = []
# Función para enmascarar fecha
def formato_fecha_keyrelease(event):
    s = entry_fecha_var.get()
    digits = ''.join(ch for ch in s if ch.isdigit())[:8]

    if len(digits) > 4:
        formatted = f"{digits[:2]}-{digits[2:4]}-{digits[4:]}"
    elif len(digits) > 2:
        formatted = f"{digits[:2]}-{digits[2:]}"
    else:
        formatted = digits

    if formatted != s:
        entry_fecha_var.set(formatted)

    entry_fecha.icursor(tk.END)

# Función para guardar en archivo
def guardar_en_archivo():
    with open("medicamento.txt", "w", encoding="utf-8") as archivo:
        for m in medicamentos_data:
            archivo.write(f"{m['Nombre']}|{m['Presentación']}|{m['Dosis']}|{m['Fecha']}\n")

# Función para cargar desde archivo
def cargar_desde_archivo():
    try:
        with open("medicamento.txt", "r", encoding="utf-8") as archivo:
            medicamentos_data.clear()
            for linea in archivo:
                partes = linea.strip().split("|")
                if len(partes) == 4:
                    m = {
                        "Nombre": partes[0],
                        "Presentación": partes[1],
                        "Dosis": partes[2],
                        "Fecha": partes[3]
                    }
                    medicamentos_data.append(m)
        cargar_treeview()
    except FileNotFoundError:
        open("medicamento.txt", "w").close()

# Función para registrar medicamento
def registrar_medicamento():
    nombre = entry_nombre.get().strip()
    presentacion = combo_presentacion.get().strip()
    dosis = entry_dosis.get().strip()
    fecha = entry_fecha_var.get().strip()

    if not (nombre and presentacion and dosis and fecha):
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        return

    m = {
        "Nombre": nombre,
        "Presentación": presentacion,
        "Dosis": dosis,
        "Fecha": fecha
    }
    medicamentos_data.append(m)
    guardar_en_archivo()
    cargar_treeview()

    # Limpiar entradas
    entry_nombre.delete(0, tk.END)
    combo_presentacion.set('')
    entry_dosis.delete(0, tk.END)
    entry_fecha_var.set('')
    
# Función para eliminar medicamento
def eliminar_medicamento():
    seleccionado = treeview.selection()
    if seleccionado:
        index = int(seleccionado[0])
        item = treeview.item(seleccionado, "values")
        if messagebox.askyesno("Eliminar", f"¿Deseas eliminar el medicamento '{item[0]}'?"):
            del medicamentos_data[index]
            guardar_en_archivo()
            cargar_treeview()
    else:
        messagebox.showwarning("Eliminar", "Selecciona un registro para eliminar.")

# Función para actualizar Treeview
def cargar_treeview():
    treeview.delete(*treeview.get_children())
    for i, m in enumerate(medicamentos_data):
        treeview.insert("", "end", iid=str(i), values=(m["Nombre"], m["Presentación"], m["Dosis"], m["Fecha"]))
        
# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Gestión de Medicamentos")
ventana.geometry("800x520")
ventana.minsize(700, 450)

# Frame del formulario
form_frame = ttk.Frame(ventana, padding=(12, 10))
form_frame.grid(row=0, column=0, sticky="ew")
form_frame.columnconfigure(0, weight=0)
form_frame.columnconfigure(1, weight=1)

# Nombre
ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky="w", padx=6, pady=6)
entry_nombre = ttk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, sticky="ew", padx=6, pady=6)

# Presentación
ttk.Label(form_frame, text="Presentación:").grid(row=1, column=0, sticky="w", padx=6, pady=6)
combo_presentacion = ttk.Combobox(form_frame, values=["Tabletas", "Jarabe", "Inyectable", "Cápsulas", "Otro"])
combo_presentacion.grid(row=1, column=1, sticky="ew", padx=6, pady=6)

# Dosis
ttk.Label(form_frame, text="Dosis:").grid(row=2, column=0, sticky="w", padx=6, pady=6)
entry_dosis = ttk.Entry(form_frame)
entry_dosis.grid(row=2, column=1, sticky="w", padx=6, pady=6)

# Fecha Vencimiento
ttk.Label(form_frame, text="Fecha Vencimiento (dd-mm-yyyy):").grid(row=3, column=0, sticky="w", padx=6, pady=6)
entry_fecha_var = tk.StringVar()
entry_fecha = ttk.Entry(form_frame, textvariable=entry_fecha_var)
entry_fecha.grid(row=3, column=1, sticky="w", padx=6, pady=6)
entry_fecha.bind("<KeyRelease>", formato_fecha_keyrelease)

# Botones
btn_frame = ttk.Frame(form_frame)
btn_frame.grid(row=4, column=0, columnspan=2, sticky="ew", padx=6, pady=(10, 2))
btn_frame.columnconfigure((0, 1), weight=1)

ttk.Button(btn_frame, text="Registrar", command=registrar_medicamento).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
ttk.Button(btn_frame, text="Eliminar", command=eliminar_medicamento).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Frame lista
list_frame = ttk.Frame(ventana, padding=(12, 6))
list_frame.grid(row=1, column=0, sticky="nsew")
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)
list_frame.rowconfigure(0, weight=1)
list_frame.columnconfigure(0, weight=1)

treeview = ttk.Treeview(list_frame, columns=("nombre", "presentacion", "dosis", "fecha"), show="headings")
treeview.grid(row=0, column=0, sticky="nsew")
treeview.heading("nombre", text="Nombre")
treeview.heading("presentacion", text="Presentación")
treeview.heading("dosis", text="Dosis")
treeview.heading("fecha", text="Fecha Vencimiento")
treeview.column("nombre", width=220)
treeview.column("presentacion", width=120, anchor="center")
treeview.column("dosis", width=100, anchor="center")
treeview.column("fecha", width=120, anchor="center")

scroll_y = ttk.Scrollbar(list_frame, orient="vertical", command=treeview.yview)
scroll_y.grid(row=0, column=1, sticky="ns")
treeview.configure(yscrollcommand=scroll_y.set)

# Cargar datos al iniciar
cargar_desde_archivo()

# Ejecutar
ventana.mainloop()


