# CRUD Tkinter

## Cómo correr el proyecto

### En Mac

1. Instalar MariaDB (si no lo tenés):
   ```
   brew install mariadb-connector-c
   brew install mariadb
   brew services start mariadb
   ```
2. Habilitar la cuenta `root` para conexión por red (una instalación nueva la deja bloqueada):
   ```
   /opt/homebrew/opt/mariadb/bin/mariadb -u $(whoami) -e "ALTER USER 'root'@'localhost' IDENTIFIED BY ''; FLUSH PRIVILEGES;"
   ```
3. Crear la base y las tablas:
   ```
   /opt/homebrew/opt/mariadb/bin/mariadb -u root -h 127.0.0.1 -P 3306 < schema.sql
   ```
4. Crear y activar el entorno virtual:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```
6. Correr el programa:
   ```
   python3 main.py
   ```
### En Windows

1. Instalar MariaDB con el instalador oficial (https://mariadb.org/download/). Durante la instalación va a pedir definir la contraseña de `root` — dejarla en blanco, o si le ponés una, ajustar `password=""` en `mariadb_repository.py` con la que hayas elegido.
2. Crear la base y las tablas: abrir HeidiSQL (viene con el instalador) o la consola `mariadb`, conectarse, y ejecutar el contenido de `schema.sql`.
3. Crear y activar el entorno virtual:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
4. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```
5. Correr el programa:
   ```
   python main.py
   ```
