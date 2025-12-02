from tkinter import *
from tkinter import messagebox

# --- CONFIGURACIÓN DE COLORES Y ESTILO ---
COLOR_FONDO = "#F3E5F5"       # Lavanda suave (Fondo ventana)
COLOR_FRAME = "#E1BEE7"       # Morado claro (Fondo de los cuadros)
COLOR_BTN = "#6A1B9A"         # Morado oscuro (Botones)
COLOR_BTN_TEXTO = "white"     # Texto de los botones
COLOR_TITULO = "#4A148C"      # Morado muy oscuro (Texto títulos)

FUENTE_TITULO = ("Helvetica", 16, "bold")
FUENTE_NORMAL = ("Helvetica", 11)

class Vista:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("..: Coches System :..")
        ventana.geometry("700x800")
        ventana.resizable(False, False)
        ventana.configure(bg=COLOR_FONDO)
        self.menu_principal(ventana)
    
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    
    @staticmethod
    def crear_boton(padre, texto, comando, bg_color=COLOR_BTN):
        """Helper para crear botones con estilo uniforme"""
        return Button(padre, text=texto, command=comando, 
                      bg=bg_color, fg=COLOR_BTN_TEXTO, 
                      font=FUENTE_NORMAL, activebackground="#8E24AA", 
                      activeforeground="white", bd=0, padx=15, pady=5, cursor="hand2")

    @staticmethod
    def crear_label(padre, texto, es_titulo=False):
        """Helper para crear etiquetas con el fondo correcto"""
        fuente = FUENTE_TITULO if es_titulo else FUENTE_NORMAL
        color_texto = COLOR_TITULO if es_titulo else "black"
        return Label(padre, text=texto, bg=COLOR_FONDO, fg=color_texto, font=fuente, justify="center")

    @staticmethod
    def menu_principal(ventana):
        Vista.borrarPantalla(ventana)
        ventana.configure(bg=COLOR_FONDO)
        
        lbl_titulo = Vista.crear_label(ventana, "..:: Menu Principal ::..", es_titulo=True)
        lbl_titulo.pack(pady=30)
        
        marco_botones = Frame(ventana, height=200, width=500, bg=COLOR_FRAME)
        marco_botones.pack_propagate(False)
        marco_botones.pack(pady=10)
        
        btn_autos = Vista.crear_boton(marco_botones, "Autos", lambda: Vista.menu_acciones(ventana, "Autos"))
        btn_autos.grid(column=0, row=0, padx=15, pady=25)
        
        btn_camionetas = Vista.crear_boton(marco_botones, "Camionetas", lambda: Vista.menu_acciones(ventana, "Camionetas"))
        btn_camionetas.grid(column=1, row=0, padx=15, pady=25)
        
        btn_camiones = Vista.crear_boton(marco_botones, "Camiones", lambda: Vista.menu_acciones(ventana, "Camiones"))
        btn_camiones.grid(column=2, row=0, padx=15, pady=25)
        
        btn_salir = Vista.crear_boton(ventana, "Salir", ventana.quit)
        btn_salir.pack(pady=40)
    
    @staticmethod
    def menu_acciones(ventana, tipo):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo = Vista.crear_label(ventana, f"..:: Menu {tipo} ::..", es_titulo=True)
        lbl_titulo.pack(pady=20)
        
        marco_botones = Frame(ventana, height=200, width=500, bg=COLOR_FRAME)
        marco_botones.pack_propagate(False)
        marco_botones.pack(pady=10)
        
        btn_insertar = Vista.crear_boton(marco_botones, "Insertar", lambda: Vista.insertar_autos(ventana, tipo))
        btn_insertar.grid(column=0, row=0, padx=20, pady=20)
        
        btn_consultar = Vista.crear_boton(marco_botones, "Consultar", lambda: Vista.consultar_autos(ventana, tipo))
        btn_consultar.grid(padx=20, pady=20, column=1, row=0)
        
        btn_actualizar = Vista.crear_boton(marco_botones, "Actualizar", lambda: Vista.buscar_autos(ventana, tipo, "cambiar"))
        btn_actualizar.grid(column=0, row=1, padx=20, pady=20)
        
        btn_eliminar = Vista.crear_boton(marco_botones, "Eliminar", lambda: Vista.buscar_autos(ventana, tipo, "borrar"))
        btn_eliminar.grid(column=1, row=1, padx=20, pady=20)
        
        btn_regresar = Vista.crear_boton(ventana, "Regresar", lambda: Vista.menu_principal(ventana))
        btn_regresar.pack(pady=30)
        
    @staticmethod
    def insertar_autos(ventana, tipo):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo = Vista.crear_label(ventana, f"..:: Insertar {tipo} ::..", es_titulo=True)
        lbl_titulo.pack(pady=15)
        
        campos = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"]
        
        for campo in campos:
            Vista.crear_label(ventana, f"{campo}:").pack(pady=2)
            Entry(ventana, font=FUENTE_NORMAL, bd=2, relief="groove").pack(pady=2)
        
        if tipo == "Camionetas":
            Vista.crear_label(ventana, "Traccion:").pack(pady=2)
            Entry(ventana, font=FUENTE_NORMAL).pack(pady=2)
            
            Vista.crear_label(ventana, "Cerrada (SI/NO):").pack(pady=2)
            Entry(ventana, font=FUENTE_NORMAL).pack(pady=2)
            
        elif tipo == "Camiones":
            Vista.crear_label(ventana, "Ejes:").pack(pady=2)
            Entry(ventana, font=FUENTE_NORMAL).pack(pady=2)
            
            Vista.crear_label(ventana, "Capacidad de Carga:").pack(pady=2)
            Entry(ventana, font=FUENTE_NORMAL).pack(pady=2)
            
        btn_guardar = Vista.crear_boton(ventana, "Guardar", lambda: messagebox.showinfo("Info", "Botón Guardar presionado"))
        btn_guardar.pack(pady=20)

        btn_regresar = Vista.crear_boton(ventana, "Regresar", lambda: Vista.menu_acciones(ventana, tipo))
        btn_regresar.pack(pady=10)
    
    @staticmethod
    def consultar_autos(ventana, tipo):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo = Vista.crear_label(ventana, f"..:: Consultar {tipo} ::..", es_titulo=True)
        lbl_titulo.pack(pady=10)
        
        filas = ""
        registros = []
        
        # Datos simulados
        if tipo == "Autos":
            registros = [(1, "Nissan", "Blanco", "2020", 200, 50, 5)]
        elif tipo == "Camionetas":
            registros = [(1, "Nissan", "Blanco", "2020", 200, 50, 5, "4x4", "SI")]
        elif tipo == "Camiones":
            registros = [(1, "Nissan", "Blanco", "2020", 200, 50, 5, 4, 1000)]
            
        num_auto = 1
        if len(registros) > 0:
            for fila in registros:
                base_info = f"\nID: {fila[0]} | Marca: {fila[1]} | Color: {fila[2]} | Modelo: {fila[3]}\nVelocidad: {fila[4]} | Caballaje: {fila[5]} | Plazas: {fila[6]}"
                
                if tipo == "Autos":
                    filas += f"AUTO #{num_auto}: {base_info}\n" + "-"*60
                elif tipo == "Camionetas":
                    filas += f"CAMIONETA #{num_auto}: {base_info}\nTraccion: {fila[7]} | Cerrada: {fila[8]}\n" + "-"*60
                elif tipo == "Camiones":
                    filas += f"CAMION #{num_auto}: {base_info}\nEje: {fila[7]} | Carga: {fila[8]}\n" + "-"*60
                num_auto += 1
        else:
            messagebox.showinfo(icon="warning", message=f"No existen {tipo} para mostrar")
            
        lbl_resultado = Label(ventana, text=filas, bg="white", fg="black", font=("Courier", 10), justify="left", bd=2, relief="sunken", padx=10, pady=10)
        lbl_resultado.pack(pady=10, padx=20)
        
        btn_regresar = Vista.crear_boton(ventana, "Regresar", lambda: Vista.menu_acciones(ventana, tipo))
        btn_regresar.pack(pady=20)
        
    @staticmethod
    def buscar_autos(ventana, tipo, accion):
        Vista.borrarPantalla(ventana)
        
        lbl_titulo = Vista.crear_label(ventana, f"..:: Buscar {tipo} ::..", es_titulo=True)
        lbl_titulo.pack(pady=20)
        
        Vista.crear_label(ventana, f"ID de {tipo} a buscar: ").pack(pady=5)
        
        id_var = IntVar()
        txt_id = Entry(ventana, textvariable=id_var, width=10, justify="center", font=FUENTE_NORMAL)
        txt_id.focus()
        txt_id.pack(pady=10)
        
        if accion == "cambiar":
            Vista.crear_boton(ventana, "Buscar", lambda: Vista.cambiar_auto(ventana, tipo)).pack(pady=10)
        elif accion == "borrar":
            Vista.crear_boton(ventana, "Buscar", lambda: Vista.eliminar_auto(ventana, tipo)).pack(pady=10)
        
        Vista.crear_boton(ventana, "Regresar", lambda: Vista.menu_acciones(ventana, tipo)).pack(pady=10)
            
    @staticmethod
    def cambiar_auto(ventana, tipo):
        registro = "Encontrado" # Simulación
        if registro is None:
            messagebox.showinfo(icon="info", message="No existe en la BD")
        else:
            Vista.borrarPantalla(ventana)
            Vista.crear_label(ventana, f".:: Cambiar {tipo} ::.", es_titulo=True).pack(pady=15)

            Vista.crear_label(ventana, "ID: ").pack(pady=2)
            id_var = IntVar()
            Entry(ventana, textvariable=id_var, width=10, justify="center", state="readonly", font=FUENTE_NORMAL).pack(pady=2)
            
            campos = ["Marca", "Color", "Modelo", "Velocidad", "Potencia", "No. Plazas"]
            for campo in campos:
                Vista.crear_label(ventana, f"{campo}: ").pack(pady=2)
                Entry(ventana, font=FUENTE_NORMAL).pack(pady=2)
            
            if tipo == "Camionetas":
                Vista.crear_label(ventana, "Traccion: ").pack(pady=2)
                Entry(ventana, font=FUENTE_NORMAL).pack(pady=2)
                Vista.crear_label(ventana, "Cerrada (SI/NO): ").pack(pady=2)
                Entry(ventana, font=FUENTE_NORMAL).pack(pady=2)
            elif tipo == "Camiones":
                Vista.crear_label(ventana, "Ejes:").pack(pady=2)
                Entry(ventana, font=FUENTE_NORMAL).pack(pady=2)
                Vista.crear_label(ventana, "Capacidad de Carga:").pack(pady=2)
                Entry(ventana, font=FUENTE_NORMAL).pack(pady=2)
            
            Vista.crear_boton(ventana, "Guardar Cambios", lambda: messagebox.showinfo("Info", "Cambios Guardados")).pack(pady=20)
            Vista.crear_boton(ventana, "Regresar", lambda: Vista.menu_acciones(ventana, tipo)).pack(pady=10)

    @staticmethod
    def eliminar_auto(ventana, tipo):
        registro = "Encontrado" # Simulación
        if registro is None:
            messagebox.showinfo(icon="info", message="No existen esta registros la BD")
        else:
            Vista.borrarPantalla(ventana)
            Vista.crear_label(ventana, f"..:: Eliminar un {tipo} ::..", es_titulo=True).pack(pady=20)

            Vista.crear_label(ventana, "ID a eliminar: ").pack(pady=5)
            id_var = IntVar()
            txt_id_eliminar = Entry(ventana, textvariable=id_var, width=10, font=FUENTE_NORMAL, justify="center")
            txt_id_eliminar.focus()
            txt_id_eliminar.pack(pady=10)

            btn_eliminar = Vista.crear_boton(ventana, "ELIMINAR DEFINITIVAMENTE", 
                                             lambda: messagebox.showinfo("Alerta", "Registro Eliminado"), 
                                             bg_color="#D32F2F")
            btn_eliminar.pack(pady=20)

            Vista.crear_boton(ventana, "Regresar", lambda: Vista.menu_acciones(ventana, tipo)).pack(pady=10)

if __name__ == "__main__":
    root = Tk()
    app = Vista(root)
    root.mainloop()