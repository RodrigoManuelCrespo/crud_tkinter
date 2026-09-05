import tkinter as tk
from tkinter import ttk
from crud import CRUDFrame
from repository import Repository


class PeliculasCRUD(CRUDFrame):
    def __init__(self, master):
        fields = [
            ("Título", "titulo"),
            ("Director", "director"),
            ("Género", "genero"),
            ("Año", "anio"),
            ("Duración", "duracion"),
        ]
        super().__init__(master, "Películas", fields, Repository())


class DirectoresCRUD(CRUDFrame):
    def __init__(self, master):
        fields = [
            ("Nombre", "nombre"),
            ("Nacionalidad", "nacionalidad"),
            ("Año de nacimiento", "anio_nacimiento"),
            ("Cantidad de películas", "cant_peliculas"),
        ]
        super().__init__(master, "Directores", fields, Repository())


def main():
    root = tk.Tk()
    root.title("Sistema CRUD")
    root.geometry("650x600")

    pestañas = ttk.Notebook(root)
    pestañas.pack(fill="both", expand=True)

    pestañas.add(PeliculasCRUD(pestañas), text="Películas")
    pestañas.add(DirectoresCRUD(pestañas), text="Directores")

    root.mainloop()


if __name__ == "__main__":
    main()
