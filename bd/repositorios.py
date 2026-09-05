from bd.conexion import obtener_conexion

class DirectorRepository:
    """Maneja las operaciones SQL de la tabla 'director'."""

    def read_all(self):
        conexion = obtener_conexion()
        if not conexion:
            return []
        cursor = conexion.cursor()
        cursor.execute("SELECT id_director, nombre, nacionalidad FROM director")
        filas = cursor.fetchall()
        conexion.close()
        
        # Formateamos el resultado como lista de diccionarios con la clave 'id' obligatoria
        return [
            {"id": fila[0], "nombre": fila[1], "nacionalidad": fila[2]}
            for fila in filas
        ]

    def create(self, valores: dict):
        conexion = obtener_conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        sql = "INSERT INTO director (nombre, nacionalidad) VALUES (?, ?)"
        cursor.execute(sql, (valores.get("nombre"), valores.get("nacionalidad")))
        conexion.commit()  # ⚠️ Guarda permanentemente los cambios en MariaDB
        conexion.close()

    def update(self, id_director: int, valores: dict):
        conexion = obtener_conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        sql = "UPDATE director SET nombre = ?, nacionalidad = ? WHERE id_director = ?"
        cursor.execute(sql, (valores.get("nombre"), valores.get("nacionalidad"), id_director))
        conexion.commit()
        conexion.close()

    def delete(self, id_director: int):
        conexion = obtener_conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        sql = "DELETE FROM director WHERE id_director = ?"
        cursor.execute(sql, (id_director,))
        conexion.commit()
        conexion.close()


class PeliculaRepository:
    """Maneja las operaciones SQL de la tabla 'pelicula'."""

    def read_all(self):
        conexion = obtener_conexion()
        if not conexion:
            return []
        cursor = conexion.cursor()
        cursor.execute("SELECT id_pelicula, titulo, anio, genero, id_director FROM pelicula")
        filas = cursor.fetchall()
        conexion.close()

        return [
            {
                "id": fila[0],
                "titulo": fila[1],
                "anio": fila[2],
                "genero": fila[3],
                "id_director": fila[4]
            }
            for fila in filas
        ]

    def create(self, valores: dict):
        conexion = obtener_conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        sql = "INSERT INTO pelicula (titulo, anio, genero, id_director) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (valores.get("titulo"), valores.get("anio"), valores.get("genero"), valores.get("id_director")))
        conexion.commit()
        conexion.close()

    def update(self, id_pelicula: int, valores: dict):
        conexion = obtener_conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        sql = "UPDATE pelicula SET titulo = ?, anio = ?, genero = ?, id_director = ? WHERE id_pelicula = ?"
        cursor.execute(sql, (valores.get("titulo"), valores.get("anio"), valores.get("genero"), valores.get("id_director"), id_pelicula))
        conexion.commit()
        conexion.close()

    def delete(self, id_pelicula: int):
        conexion = obtener_conexion()
        if not conexion:
            return
        cursor = conexion.cursor()
        sql = "DELETE FROM pelicula WHERE id_pelicula = ?"
        cursor.execute(sql, (id_pelicula,))
        conexion.commit()
        conexion.close()