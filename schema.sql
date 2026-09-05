
CREATE DATABASE IF NOT EXISTS crud_tkinter;

USE crud_tkinter;

CREATE TABLE peliculas (
    id INT NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(128) NOT NULL,
    director VARCHAR(128) NOT NULL,
    genero VARCHAR(64) NOT NULL,
    anio INT NOT NULL,
    duracion INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE directores (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(128) NOT NULL,
    nacionalidad VARCHAR(64) NOT NULL,
    anio_nacimiento INT NOT NULL,
    cant_peliculas INT NOT NULL,
    PRIMARY KEY (id)
);
