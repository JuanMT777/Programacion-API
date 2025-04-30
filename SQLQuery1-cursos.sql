CREATE DATABASE GestionEstudiantesCursos;
GO

USE GestionEstudiantesCursos;
GO

CREATE TABLE Estudiantes (
    id_estudiante VARCHAR(20) PRIMARY KEY,
    nombre_completo VARCHAR(100),
    correo VARCHAR(100)
);

CREATE TABLE Cursos (
    id_curso VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    creditos INT
);

CREATE TABLE Inscripciones (
    id_estudiante VARCHAR(20),
    id_curso VARCHAR(20),
    PRIMARY KEY (id_estudiante, id_curso),
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);


SELECT TOP 1 * FROM Cursos
