import tkinter as tk
from tkinter import ttk
from crud import CRUDFrame
from mariadb_repository import MariaDBRepository


class PeliculasCRUD(CRUDFrame):
    def __init__(self, contenedor):
        campos = [
            {"label": "Título", "columna": "titulo"},
            {"label": "Director", "columna": "director"},
            {"label": "Género", "columna": "genero"},
            {"label": "Año", "columna": "anio"},
            {"label": "Duración", "columna": "duracion"},
        ]
        columnas = []
        for campo in campos:
            columnas.append(campo["columna"])
        repositorio = MariaDBRepository(table="peliculas", columns=columnas)
        super().__init__(contenedor, "Películas", campos, repositorio)


class DirectoresCRUD(CRUDFrame):
    def __init__(self, contenedor):
        campos = [
            {"label": "Nombre", "columna": "nombre"},
            {"label": "Nacionalidad", "columna": "nacionalidad"},
            {"label": "Año de nacimiento", "columna": "anio_nacimiento"},
            {"label": "Cantidad de películas", "columna": "cant_peliculas"},
        ]
        columnas = []
        for campo in campos:
            columnas.append(campo["columna"])
        repositorio = MariaDBRepository(table="directores", columns=columnas)
        super().__init__(contenedor, "Directores", campos, repositorio)


def main():
    # crea ventana
    root = tk.Tk()
    root.title("Sistema CRUD")
    root.geometry("650x600")

    # crea los tabs
    pestañas = ttk.Notebook(root)
    # fill llena ejes x e y, expand si se agranda la pantalla que ocupe todo el ancho
    pestañas.pack(fill="both", expand=True)
    # ejecuta el init de pelicula, una vez generado eso
    pestañas.add(PeliculasCRUD(pestañas), text="Películas")
    pestañas.add(DirectoresCRUD(pestañas), text="Directores")

    root.mainloop()


if __name__ == "__main__":
    main()
