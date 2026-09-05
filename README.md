# CRUD Tkinter
## Cómo correr el proyecto
### python3 -m venv venv              # crea su propio venv vacío
### source venv/bin/activate          # lo activa (en Windows: venv\Scripts\activate)
### pip install -r requirements.txt   # lee el archivo e instala TODO
### python3 main.py                   # corre el proyecto

## Base de datos (MariaDB)

Cada persona del equipo corre su propia base local (no es compartida). Pasos, una sola vez, **antes** del primer `python3 main.py`:

### En Mac (Homebrew)

1. Instalar la librería cliente (necesaria para que `pip install mariadb` compile):
   ```
   brew install mariadb-connector-c
   ```
2. Instalar y arrancar el servidor MariaDB:
   ```
   brew install mariadb
   brew services start mariadb
   ```
3. **Importante:** una instalación nueva de MariaDB deja la cuenta `root` bloqueada para conexiones por red (contraseña marcada como `invalid`). Habilitarla:
   ```
   /opt/homebrew/opt/mariadb/bin/mariadb -u $(whoami) -e "ALTER USER 'root'@'localhost' IDENTIFIED BY ''; FLUSH PRIVILEGES;"
   ```
4. Crear la base y las tablas:
   ```
   /opt/homebrew/opt/mariadb/bin/mariadb -u root -h 127.0.0.1 -P 3306 < schema.sql
   ```

⚠️ Si ya tenés otro MySQL/MariaDB corriendo en el puerto 3306 (por ejemplo, uno instalado con el instalador oficial de Oracle), va a chocar con este. Hay que detener el otro servicio primero.

### En Windows

Instalar MariaDB con el instalador oficial (https://mariadb.org/download/). El instalador de Windows normalmente pide definir la contraseña de `root` durante la instalación (a diferencia de Homebrew) — usar una en blanco o ajustar `password=""` en `mariadb_repository.py` según lo que hayan definido. Después, ejecutar `schema.sql` desde HeidiSQL (viene incluido con el instalador) o desde la consola `mariadb`.

### Verificar que quedó bien

```
/opt/homebrew/opt/mariadb/bin/mariadb -u root -h 127.0.0.1 -P 3306 -e "USE crud_tkinter; SHOW TABLES;"
```
Debería listar `peliculas` y `directores`. También se puede usar MySQL Workbench, TablePlus o Sequel Ace apuntando a `127.0.0.1:3306`, usuario `root`, sin contraseña.
