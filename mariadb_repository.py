import sys

import mariadb

class MariaDBRepository:
    def __init__(self, table, columns, host="127.0.0.1", port=3306,
                 user="root", password="", database="crud_tkinter"):
        self.table = table
        self.columns = columns

        try:
            self.conexion = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database,
            )
            self.cursor = self.conexion.cursor()
        except mariadb.Error as error:
            print(f"Error al conectar con la base de datos: {error}")
            sys.exit(1)

    def create(self, data):
        columnas = ", ".join(self.columns)
        placeholders = ", ".join("?" for _ in self.columns)
        valores = tuple(data[columna] for columna in self.columns)
        try:
            self.cursor.execute(
                f"INSERT INTO {self.table}({columnas}) VALUES({placeholders})",
                valores,
            )
            self.conexion.commit()
        except mariadb.Error as error:
            print(f"Error al crear el registro: {error}")

    def read_all(self):
        try:
            # ejecuta la query con el select devolviendo todos los datos de la tabla
            self.cursor.execute(f"SELECT id, {', '.join(self.columns)} FROM {self.table}")
            # ejecuta la consulta y devuelve todo en forma de tupla
            filas = self.cursor.fetchall()
        except mariadb.Error as error:
            print(f"Error al leer los registros: {error}")
            return []
        resultado = []
        for fila in filas:
            item = {"id": fila[0]}
            for indice, columna in enumerate(self.columns):
                item[columna] = fila[indice + 1]
            resultado.append(item)
        return resultado

    def update(self, item_id, data):
        asignaciones = ", ".join(f"{columna} = ?" for columna in self.columns)
        valores = tuple(data[columna] for columna in self.columns) + (item_id,)
        try:
            self.cursor.execute(
                f"UPDATE {self.table} SET {asignaciones} WHERE id = ?",
                valores,
            )
            self.conexion.commit()
        except mariadb.Error as error:
            print(f"Error al actualizar el registro: {error}")

    def delete(self, item_id):
        try:
            self.cursor.execute(f"DELETE FROM {self.table} WHERE id = ?", (item_id,))
            self.conexion.commit()
        except mariadb.Error as error:
            print(f"Error al eliminar el registro: {error}")
