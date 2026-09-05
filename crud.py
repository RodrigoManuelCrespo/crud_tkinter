import tkinter as tk
from tkinter import messagebox


class CRUDFrame(tk.Frame):
    def __init__(self, master, entity_name: str, fields, repository):
        super().__init__(master)
        self.entity_name = entity_name
        self.fields = fields
        self.repository = repository
        self.entries = {}
        self.selected_id = None

        bienvenida = tk.Label(self, text=f"Gestión de {entity_name}", font=("Arial", 14, "bold"))
        bienvenida.pack(pady=10)

        self._crear_formulario()
        self._crear_botones()
        self._crear_lista()

        self._refrescar_lista()

    def _crear_formulario(self):
        marco = tk.LabelFrame(self, text="Datos", padx=10, pady=10)
        marco.pack(padx=10, pady=5, fill="x")

        for fila, (texto, clave) in enumerate(self.fields):
            tk.Label(marco, text=texto).grid(row=fila, column=0, sticky="w", pady=2)
            entrada = tk.Entry(marco, width=30)
            entrada.grid(row=fila, column=1, pady=2)
            self.entries[clave] = entrada

    def _crear_lista(self):
        marco = tk.LabelFrame(self, text=f"{self.entity_name} cargados", padx=10, pady=10)
        marco.pack(padx=10, pady=5, fill="both", expand=True)

        self.lista = tk.Listbox(marco)
        self.lista.pack(fill="both", expand=True)
        self.lista.bind("<<ListboxSelect>>", self._seleccionar_item)

    def _crear_botones(self):
        marco = tk.Frame(self)
        marco.pack(pady=10)

        tk.Button(marco, text="Crear", width=10, command=self._crear).grid(row=0, column=0, padx=5)
        tk.Button(marco, text="Actualizar", width=10, command=self._actualizar).grid(row=0, column=1, padx=5)
        tk.Button(marco, text="Eliminar", width=10, command=self._eliminar).grid(row=0, column=2, padx=5)
        tk.Button(marco, text="Limpiar", width=10, command=self._limpiar).grid(row=0, column=3, padx=5)

    def _obtener_valores(self):
        return {clave: entrada.get().strip() for clave, entrada in self.entries.items()}

    def _hay_campos_vacios(self, valores):
        return any(valor == "" for valor in valores.values())

    def _refrescar_lista(self):
        self.lista.delete(0, tk.END)
        for item in self.repository.read_all():
            resumen = " | ".join(str(item.get(clave, "")) for _, clave in self.fields)
            self.lista.insert(tk.END, f"#{item['id']} - {resumen}")

    def _seleccionar_item(self, event):
        seleccion = self.lista.curselection()
        if not seleccion:
            return
        indice = seleccion[0]
        item = self.repository.read_all()[indice]
        self.selected_id = item["id"]
        for clave, entrada in self.entries.items():
            entrada.delete(0, tk.END)
            entrada.insert(0, item.get(clave, ""))

    def _crear(self):
        valores = self._obtener_valores()
        if self._hay_campos_vacios(valores):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        self.repository.create(valores)
        self._refrescar_lista()
        self._limpiar()

    def _actualizar(self):
        if self.selected_id is None:
            messagebox.showerror("Error", "Seleccioná un registro de la lista antes de actualizar.")
            return
        valores = self._obtener_valores()
        if self._hay_campos_vacios(valores):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        self.repository.update(self.selected_id, valores)
        self._refrescar_lista()
        self._limpiar()

    def _eliminar(self):
        if self.selected_id is None:
            messagebox.showerror("Error", "Seleccioná un registro de la lista antes de eliminar.")
            return
        self.repository.delete(self.selected_id)
        self._refrescar_lista()
        self._limpiar()

    def _limpiar(self):
        for entrada in self.entries.values():
            entrada.delete(0, tk.END)
        self.selected_id = None
        self.lista.selection_clear(0, tk.END)
