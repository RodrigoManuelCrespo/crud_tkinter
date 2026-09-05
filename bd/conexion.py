import mariadb
import sys

# Configuración de parámetros de conexión a XAMPP
CONFIG_CONEXION = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",  # Contraseña vacía por defecto en XAMPP
    "port": 3306
}

def obtener_conexion():
    """Devuelve una conexión activa a la base de datos 'cine_db'."""
    try:
        conexion = mariadb.connect(**CONFIG_CONEXION, database="cine_db")
        return conexion
    except mariadb.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def inicializar_bd():
    """
    Crea la Base de Datos 'cine_db' y las tablas 'director' y 'pelicula' 
    si no existen aún.
    """
    try:
        # 1. Conexión inicial al servidor sin especificar la base de datos
        conexion = mariadb.connect(**CONFIG_CONEXION)
        cursor = conexion.cursor()

        # 2. Crear la Base de Datos
        cursor.execute("CREATE DATABASE IF NOT EXISTS cine_db;")
        cursor.execute("USE cine_db;")
        print("✅ Base de datos 'cine_db' verificada.")

        # 3. Crear Tabla 'director'
        sql_director = """
        CREATE TABLE IF NOT EXISTS director (
            id_director INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            nacionalidad VARCHAR(50)
        );
        """
        cursor.execute(sql_director)
        print("✅ Tabla 'director' creada o verificada.")

        # 4. Crear Tabla 'pelicula' con Clave Foránea
        sql_pelicula = """
        CREATE TABLE IF NOT EXISTS pelicula (
            id_pelicula INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(150) NOT NULL,
            anio INT,
            genero VARCHAR(50),
            id_director INT,
            FOREIGN KEY (id_director) REFERENCES director(id_director) 
            ON DELETE CASCADE ON UPDATE CASCADE
        );
        """
        cursor.execute(sql_pelicula)
        print("✅ Tabla 'pelicula' creada o verificada.")

        conexion.commit()
        conexion.close()
        print("🚀 Base de datos inicializada correctamente.")

    except mariadb.Error as e:
        print(f"❌ Error durante la inicialización de la BD: {e}")

# Si ejecutas este archivo directamente, se creará la BD
if __name__ == "__main__":
    inicializar_bd()