import tkinter as tk
from tkinter import ttk
from crud import CRUDFrame
from bd.conexion import inicializar_bd
from bd.repositorios import DirectorRepository, PeliculaRepository


class PeliculasCRUD(CRUDFrame):
    def __init__(self, master):
        # Campos de la tabla 'pelicula' en MariaDB
        fields = [
            ("Título", "titulo"),
            ("Año", "anio"),
            ("Género", "genero"),
            ("Duracion", "Duracion"),
        ]
        # Conectamos con el repositorio real de Películas
        super().__init__(master, "Películas", fields, PeliculaRepository())


class DirectoresCRUD(CRUDFrame):
    def __init__(self, master):
        # Campos de la tabla 'director' en MariaDB
        fields = [
            ("Nombre", "nombre"),
            ("Nacionalidad", "nacionalidad"),
        ]
        # Conectamos con el repositorio real de Directores
        super().__init__(master, "Directores", fields, DirectorRepository())


def lanzar_aplicacion():
    # 1. Aseguramos que la base de datos y tablas existan en XAMPP/MariaDB
    inicializar_bd()

    # 2. Creación de la ventana principal
    root = tk.Tk()
    root.title("Sistema CRUD - Cine")
    root.geometry("650x600")

    # 3. Creación del panel de pestañas
    pestañas = ttk.Notebook(root)
    pestañas.pack(fill="both", expand=True)

    # 4. Agregar cada vista CRUD a sus respectivas pestañas
    pestañas.add(PeliculasCRUD(pestañas), text="Películas")
    pestañas.add(DirectoresCRUD(pestañas), text="Directores")

    # 5. Iniciar la aplicación
    root.mainloop()


if __name__ == "__main__":
    lanzar_aplicacion()