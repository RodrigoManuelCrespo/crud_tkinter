import tkinter as tk
from tkinter import messagebox


class CRUDFrame(tk.Frame):
    def __init__(self, contenedor, nombre_entidad, campos, bd):
        super().__init__(contenedor)
        self.nombre_entidad = nombre_entidad
        self.campos = campos
        self.bd = bd
        self.entries = {}
        self.selected_id = None

        bienvenida = tk.Label(self, text=f"Gestión de {nombre_entidad}", font=("Arial", 14, "bold"))
        bienvenida.pack(pady=10)

        self.crear_formulario()
        self.crear_botones()
        self.crear_lista()
        self.refrescar_lista()

    def crear_formulario(self):
        marco = tk.LabelFrame(self, text="Datos", padx=10, pady=10)
        marco.pack(padx=10, pady=5, fill="x")

        for fila, campo in enumerate(self.campos):
            tk.Label(marco, text=campo["label"]).grid(row=fila, column=0, sticky="w", pady=2)
            entrada = tk.Entry(marco, width=30)
            entrada.grid(row=fila, column=1, pady=2)
            self.entries[campo["columna"]] = entrada

    def crear_lista(self):
        marco = tk.LabelFrame(self, text=f"{self.nombre_entidad} cargados", padx=10, pady=10)
        marco.pack(padx=10, pady=5, fill="both", expand=True)

        titulos = ["ID"]
        for campo in self.campos:
            titulos.append(campo["label"])
        encabezado = " | ".join(titulos)
        tk.Label(marco, text=encabezado, font=("Arial", 10, "bold")).pack(fill="x")

        self.lista = tk.Listbox(marco)
        self.lista.pack(fill="both", expand=True)
        self.lista.bind("<<ListboxSelect>>", self.seleccionar_item)

    def crear_botones(self):
        marco = tk.Frame(self)
        marco.pack(pady=10)

        tk.Button(marco, text="Crear", width=10, command=self.crear).grid(row=0, column=0, padx=5)
        tk.Button(marco, text="Actualizar", width=10, command=self.actualizar).grid(row=0, column=1, padx=5)
        tk.Button(marco, text="Eliminar", width=10, command=self.eliminar).grid(row=0, column=2, padx=5)
        tk.Button(marco, text="Limpiar", width=10, command=self.limpiar).grid(row=0, column=3, padx=5)

    def refrescar_lista(self):
        self.lista.delete(0, tk.END)
        for item in self.bd.read_all():
            valores_texto = []
            for campo in self.campos:
                valores_texto.append(str(item.get(campo["columna"], "")))
            resumen = " | ".join(valores_texto)
            self.lista.insert(tk.END, f"#{item['id']} - {resumen}")

    def seleccionar_item(self, event):
        seleccion = self.lista.curselection()
        if not seleccion:
            return
        indice = seleccion[0]
        item = self.bd.read_all()[indice]
        self.selected_id = item["id"]
        for clave, entrada in self.entries.items():
            entrada.delete(0, tk.END)
            entrada.insert(0, item.get(clave, ""))

    def crear(self):
        valores = self.obtener_valores()
        if self.hay_campos_vacios(valores):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        self.bd.create(valores)
        self.refrescar_lista()
        self.limpiar()

    def actualizar(self):
        if self.selected_id is None:
            messagebox.showerror("Error", "Seleccioná un registro de la lista antes de actualizar.")
            return
        valores = self.obtener_valores()
        if self.hay_campos_vacios(valores):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        self.bd.update(self.selected_id, valores)
        self.refrescar_lista()
        self.limpiar()

    def eliminar(self):
        if self.selected_id is None:
            messagebox.showerror("Error", "Seleccioná un registro de la lista antes de eliminar.")
            return
        self.bd.delete(self.selected_id)
        self.refrescar_lista()
        self.limpiar()

    def limpiar(self):
        for entrada in self.entries.values():
            entrada.delete(0, tk.END)
        self.selected_id = None
        self.lista.selection_clear(0, tk.END)

    def obtener_valores(self):
        return {clave: entrada.get().strip() for clave, entrada in self.entries.items()}

    def hay_campos_vacios(self, valores):
        return any(valor == "" for valor in valores.values())
